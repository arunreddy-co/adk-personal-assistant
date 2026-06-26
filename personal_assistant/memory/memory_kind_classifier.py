from google import genai

from personal_assistant.memory.json_utils import (
    parse_json_response
)

client = genai.Client(
    vertexai=True
)


def classify_memory_kind(
    text: str
):
    """
    Decide which memory system
    should handle this message.
    """

    prompt = f"""
You are a memory routing classifier.

Your job is to determine which
memory system should process
a user message.

Available memory kinds:

SEMANTIC
EPISODE
BOTH
IGNORE

Definitions:

SEMANTIC:

Long-term facts, preferences,
skills, interests, goals,
identity information,
project state.

Examples:

- I am learning Rust
- My favorite editor is Cursor
- I use Gemini
- I prefer Linux


EPISODE:

Meaningful events, milestones,
actions, completed work,
important decisions,
project progress.

Examples:

- I completed merge memory
- I spent 3 hours debugging retrieval
- I shipped version 1
- I finished the reflection system


BOTH:

The message creates both
a semantic memory and
an episodic memory.

Examples:

- I decided to build an AI startup
- I changed my career goal
- I started learning quantum computing seriously


IGNORE:

Not useful to remember.

Examples:

- Hello
- Thanks
- Good morning
- How are you


Message:

{text}


Rules:

1. Facts and preferences are SEMANTIC.

2. Completed work and meaningful
   actions are EPISODE.

3. Major decisions that affect
   future identity, goals,
   or direction are BOTH.

4. Greetings and small talk
   are IGNORE.

5. Choose ONLY one kind.

Return ONLY valid JSON.

Schema:

{{
  "memory_kind":
      "SEMANTIC"
      |
      "EPISODE"
      |
      "BOTH"
      |
      "IGNORE",

  "reason":
      string
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = parse_json_response(
        response.text
    )

    return result
