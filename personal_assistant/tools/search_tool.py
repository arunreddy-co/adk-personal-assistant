from ddgs import DDGS
from personal_assistant.tools.tool_base import safe_tool


@safe_tool
def search_web(query: str):

    results_text = ""

    with DDGS() as ddgs:

        for i, r in enumerate(ddgs.text(query, max_results=5), start=1):

            results_text += f"""
Result {i}
Title: {r.get('title')}
URL: {r.get('href')}
Snippet: {r.get('body')}

"""

    return results_text
