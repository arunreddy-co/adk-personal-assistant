from google import genai

from personal_assistant.memory.json_utils import (
    parse_json_response
)

client = genai.Client(
    vertexai=True
)


def rank_memories(
    question: str,
    memories: list[str]
):
    """
    Select only the memories
    relevant to the user's question.
    """

    if not memories:
        return []

    memory_text = "\n".join(
        memories
    )

    prompt = f"""
You are a memory ranking agent.

Question:

{question}

Candidate Memories:

{memory_text}

Select the MINIMUM number of memories
required to answer the question.

Prefer 1 memory.

Only return additional memories
if they are absolutely necessary.

Return ONLY JSON.

Schema:

{{
  "relevant_memories": [
    "memory text",
    "memory text"
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

    return result.get(
        "relevant_memories",
        []
    )
