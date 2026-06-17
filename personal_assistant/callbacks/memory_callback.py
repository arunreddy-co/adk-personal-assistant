from personal_assistant.memory.memory_hook import (
    process_user_message
)


async def memory_callback(
    **kwargs
):

    try:

        callback_context = kwargs.get(
            "callback_context"
        )

        if not callback_context:
            return None

        user_content = callback_context.user_content

        if not user_content:
            return None

        if not user_content.parts:
            return None

        text = user_content.parts[0].text

        if not text:
            return None

        process_user_message(text)

    except Exception as e:

        print(
            f"[MEMORY CALLBACK ERROR] {e}"
        )

    return None
