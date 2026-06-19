from google import genai

from personal_assistant.memory.json_utils import (
    parse_json_response
)

client = genai.Client(
    vertexai=True
)


def classify_retrieval(
    question: str
):

    prompt = f"""
You are a memory retrieval classifier.

Question:

{question}

Determine which memory categories
should be retrieved.

Examples:

Question:
What is my favorite editor?

Output:
{{
  "categories": [
    "favorite_editor"
  ]
}}

Question:
What am I learning?

Output:
{{
  "categories": [
    "learning_topic"
  ]
}}

Question:
Where do I live?

Output:
{{
  "categories": [
    "location"
  ]
}}

Question:
What do you know about me?

Output:
{{
  "categories": [
    "all"
  ]
}}

Return ONLY valid JSON.

Schema:

{{
  "categories": [
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
        "categories",
        []
    )
