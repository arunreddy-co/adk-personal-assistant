from google.adk.agents import Agent

from personal_assistant.tools.search_tool import search_web
from personal_assistant.tools.test_tool import test_tool
from personal_assistant.tools.time_tool import get_current_time
from personal_assistant.tools.memory_tool import (
    remember_user_fact,
    get_user_fact_memory,
    remember_project_fact,
    get_project_fact_memory,
    list_user_memories,
    list_project_memories
)


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant.",
    instruction="""
You are a helpful assistant.

You have access to memory tools.

You can store user information using remember_user_fact.

You can retrieve user information using get_user_fact_memory.

You can store project information using remember_project_fact.

You can retrieve project information using get_project_fact_memory.

When users ask what you remember about them,
use list_user_memories.

When users ask what you know about the project,
use list_project_memories.

When users ask to remember information,
use the appropriate memory tool.

When users ask about previously stored information,
retrieve it using the appropriate memory tool.

Use tools whenever appropriate.

When users ask for current information,
people, companies, recent events,
or facts that may have changed,
use search_web.
""",
    tools=[
        test_tool,
        get_current_time,
        search_web,

	remember_user_fact,
	get_user_fact_memory,

	remember_project_fact,
	get_project_fact_memory,

	list_user_memories,
	list_project_memories
    ]
)
