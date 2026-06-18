import json

from google import genai

from personal_assistant.memory.json_utils import (
    parse_json_response
)

from personal_assistant.memory.memory_category_normalizer import (
    normalize_category
)

client = genai.Client(
    vertexai=True
)


def classify_memory_llm(
    text: str
):

    prompt = f"""
You are a memory classifier.

Determine whether the following message
should be stored as memory.

Message:
{text}

Rules:

1. Store long-term user preferences.
2. Store long-term user facts.
3. Store project facts.
4. Ignore greetings.
5. Ignore casual conversation.
6. Ignore temporary information.

Examples:

{{
  "remember": true,
  "memory_type": "user",
  "category": "favorite_editor",
  "value": "Vim"
}}

{{
  "remember": true,
  "memory_type": "user",
  "category": "learning_topic",
  "value": "Rust"
}}

{{
  "remember": true,
  "memory_type": "project",
  "category": "current_phase",
  "value": "Memory Layer"
}}

{{
  "remember": false,
  "memory_type": null,
  "category": null,
  "value": null
}}

Return ONLY valid JSON.

Schema:

{{
  "remember": true,
  "memory_type": "user" | "project" | null,
  "category": string | null,
  "value": string | null
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = parse_json_response(
        response.text
    )

    if result.get(
        "category"
    ):
        result["category"] = (
            normalize_category(
                result["category"]
            )
        )

    return result
