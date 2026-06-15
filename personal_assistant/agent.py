from google.adk.agents import Agent
from personal_assistant.tools.search_tool import search_web
from personal_assistant.tools.test_tool import test_tool
from personal_assistant.tools.time_tool import get_current_time


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant.",
    instruction="""
You are a helpful assistant.

Use tools whenever appropriate.

When users ask for current information,
people, companies, recent events,
or facts that may have changed,
use search_web.
""",
    tools=[
        test_tool,
        get_current_time,
        search_web
    ]
)
