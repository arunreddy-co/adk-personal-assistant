from google import genai

from personal_assistant.memory.json_utils import (
    parse_json_response
)

client = genai.Client(
    vertexai=True
)


def classify_memory_domains(
    question: str
):
    """
    Determine which memory domains
    should be searched.
    """

    prompt = f"""
You are a memory domain classifier.

Question:

{question}

Available memory domains:

PROFILE
PROJECT
REFLECTION
EPISODE
GOAL

Definitions:

PROFILE:
User preferences, facts,
skills, interests, location,
learning topics.

PROJECT:
Project information,
current phase, project name,
technical work.

REFLECTION:
High-level conclusions
generated from memories.

EPISODE:
Past events and actions.

GOAL:
Future objectives,
plans and ambitions.

Examples:

Question:
What is my favorite editor?

Output:
{{
  "memory_types": [
    "PROFILE"
  ]
}}

Question:
What am I learning?

Output:
{{
  "memory_types": [
    "PROFILE"
  ]
}}

Question:
What project am I working on?

Output:
{{
  "memory_types": [
    "PROJECT"
  ]
}}

Question:
What do you know about me?

Output:
{{
  "memory_types": [
    "PROFILE",
    "PROJECT",
    "REFLECTION"
  ]
}}

Return ONLY valid JSON.

Schema:

{{
  "memory_types": [
    string
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
        "memory_types",
        []
    )
