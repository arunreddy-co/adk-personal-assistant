import json


def clean_json_response(text: str):

    text = text.strip()

    if text.startswith("```json"):
        text = text[7:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def parse_json_response(text: str):

    cleaned = clean_json_response(
        text
    )

    return json.loads(
        cleaned
    )
