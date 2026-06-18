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
You are a memory action classifier.

Analyze the message and determine
what memory action should occur.

Message:
{text}

Available actions:

CREATE
UPDATE
MERGE
DELETE
IGNORE

Action Definitions:

CREATE:
A new memory that does not exist yet.

UPDATE:
An existing memory should be updated
because the user changed it.

MERGE:
New information should be merged with
existing memory.

DELETE:
A previously stored memory is no longer
valid and should be removed.

IGNORE:
Not worth remembering.

Rules:

1. Store long-term preferences.
2. Store long-term user facts.
3. Store project facts.
4. Ignore greetings.
5. Ignore casual conversation.
6. Ignore temporary information.
7. Prefer UPDATE when a user changes
   an existing preference.
8. Prefer CREATE when information is new.

Examples:

Message:
My favorite editor is Vim

Output:

{{
  "action": "CREATE",
  "memory_type": "user",
  "category": "favorite_editor",
  "value": "Vim"
}}

Message:
I switched from Vim to Cursor

Output:

{{
  "action": "UPDATE",
  "memory_type": "user",
  "category": "favorite_editor",
  "value": "Cursor"
}}

Message:
I am learning Rust

Output:

{{
  "action": "CREATE",
  "memory_type": "user",
  "category": "learning_topic",
  "value": "Rust"
}}

Message:
Current project phase is Memory Layer

Output:

{{
  "action": "CREATE",
  "memory_type": "project",
  "category": "current_phase",
  "value": "Memory Layer"
}}

Message:
Hello there

Output:

{{
  "action": "IGNORE",
  "memory_type": null,
  "category": null,
  "value": null
}}

Return ONLY valid JSON.

Schema:

{{
  "action": "CREATE" | "UPDATE" | "MERGE" | "DELETE" | "IGNORE",

  "memory_type":
      "user"
      |
      "project"
      |
      null,

  "category":
      string
      |
      null,

  "value":
      string
      |
      null
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = parse_json_response(
        response.text
    )

    if "action" not in result:

        result["action"] = "IGNORE"

    if result.get(
        "category"
    ):

        result["category"] = (
            normalize_category(
                result["category"]
            )
        )

    return result
