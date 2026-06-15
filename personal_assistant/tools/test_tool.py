from personal_assistant.tools.tool_base import safe_tool


@safe_tool
def test_tool():

    print("TEST TOOL EXECUTED")

    return "Tool executed successfully"
