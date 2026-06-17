from google.adk.agents import Agent

from personal_assistant.tools.search_tool import search_web
from personal_assistant.tools.test_tool import test_tool
from personal_assistant.tools.time_tool import get_current_time
from personal_assistant.callbacks.memory_callback import (
    memory_callback
)
from personal_assistant.callbacks.retrieval_callback import (
    retrieval_callback
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant.",
    before_agent_callback=memory_callback,
    before_model_callback=retrieval_callback,
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
