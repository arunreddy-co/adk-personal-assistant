from google import genai

from personal_assistant.memory.json_utils import (
    parse_json_response
)

client = genai.Client(
    vertexai=True
)


def classify_episode(
    text: str
):
    """
    Determine whether a message
    should be stored as an episode.
    """

    prompt = f"""
You are an episodic memory classifier.

Your job is to determine whether
a user message should be stored
as an episodic memory.

An episodic memory represents:

- A meaningful action
- A milestone
- A decision
- A completed task
- A started task
- A learned lesson
- A meaningful obstacle
- A project event
- A significant personal event

Do NOT store:

- Greetings
- Casual conversation
- Small talk
- Simple acknowledgements
- Temporary observations
- Messages with no long-term value

Summary must be grounded.

Do not invent details.

Do not infer project names.

Do not create events not present in the message.

The summary should be a concise rewrite of the user's words.

Message:

{text}

Memory Types:

PROFILE
PROJECT
BOTH

Definitions:

PROFILE:
Personal growth,
skills,
learning,
preferences,
life decisions.

PROJECT:
Project work,
technical work,
building,
debugging,
milestones,
architecture decisions.

BOTH:
Important events that affect
both the user's personal life
and project direction.

Importance Levels:

LOW:
Minor useful event.

MEDIUM:
Meaningful activity.

HIGH:
Major milestone or achievement.

CRITICAL:
Major change in direction,
life decision,
project pivot,
or highly significant event.

Examples:

Message:
I finished implementing merge memory.

Output:

{{
  "store_episode": true,
  "summary": "Implemented merge memory",
  "importance": "HIGH",
  "memory_type": "PROJECT",
  "reason": "Represents a completed project milestone"
}}

Message:
I spent three hours debugging retrieval.

Output:

{{
  "store_episode": true,
  "summary": "Debugged retrieval system",
  "importance": "MEDIUM",
  "memory_type": "PROJECT",
  "reason": "Represents meaningful project work"
}}

Message:
I decided to build an AI startup.

Output:

{{
  "store_episode": true,
  "summary": "Decided to build an AI startup",
  "importance": "CRITICAL",
  "memory_type": "BOTH",
  "reason": "Major personal and project direction decision"
}}

Message:
Hello there.

Output:

{{
  "store_episode": false,
  "summary": null,
  "importance": null,
  "memory_type": null,
  "reason": "Greeting"
}}

Return ONLY valid JSON.

Schema:

{{
  "store_episode": boolean,

  "summary":
      string
      |
      null,

  "importance":
      "LOW"
      |
      "MEDIUM"
      |
      "HIGH"
      |
      "CRITICAL"
      |
      null,

  "memory_type":
      "PROFILE"
      |
      "PROJECT"
      |
      "BOTH"
      |
      null,

  "reason":
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

    return result
