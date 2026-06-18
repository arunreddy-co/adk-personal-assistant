import json

from google import genai

from personal_assistant.memory.memory_manager import (
    get_all_user_memories,
    get_all_project_memories
)

from personal_assistant.memory.json_utils import (
    parse_json_response
)

from personal_assistant.memory.reflection_manager import (
    save_reflection
)

client = genai.Client(
    vertexai=True
)


def generate_reflections():

    user_memories = (
        get_all_user_memories()
    )

    project_memories = (
        get_all_project_memories()
    )

    memory_text = ""

    memory_text += "User Memories:\n"

    for _, key, value in user_memories:

        memory_text += (
            f"- {key}: {value}\n"
        )

    memory_text += "\n"

    memory_text += "Project Memories:\n"

    for _, key, value in project_memories:

        memory_text += (
            f"- {key}: {value}\n"
        )

    prompt = f"""
You are a memory reflection agent.

Analyze the memories below.

Generate 1 to 3 higher-level insights.

Do not repeat memories verbatim.

Find patterns.

Memories:

{memory_text}

Return ONLY JSON.

{{
  "reflections": [
    "...",
    "...",
    "..."
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = parse_json_response(
        response.text
    )


    for reflection in result["reflections"]:

        save_reflection(
            reflection
        )
    return result
