from google.adk.plugins.base_plugin import BasePlugin

from personal_assistant.memory.memory_hook import (
    process_user_message
)


class MemoryPlugin(BasePlugin):

    async def on_user_message_callback(
        self,
        *,
        invocation_context,
        user_message
    ):

        try:

            text = str(user_message)

            process_user_message(text)

        except Exception as e:

            print(
                f"[MEMORY PLUGIN ERROR] {e}"
            )

        return None
