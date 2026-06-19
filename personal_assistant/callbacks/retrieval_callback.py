from google.genai import types

from personal_assistant.memory.memory_retrieval_service import (
    retrieve_relevant_memory
)

from personal_assistant.memory.memory_inspector import (
    build_memory_summary
)


async def retrieval_callback(
    callback_context,
    llm_request
):
    """
    Inject relevant memories into the prompt
    before Gemini receives the request.
    """

    print("\n===== RETRIEVAL CALLBACK =====")

    try:

        if not llm_request.contents:
            return None

        latest_message = None

        for content in reversed(
            llm_request.contents
        ):

            if content.role == "user":

                if (
                    content.parts
                    and
                    content.parts[0].text
                ):

                    latest_message = (
                        content.parts[0].text
                    )

                    break

        if not latest_message:
            return None

        print(
            f"[USER MESSAGE] {latest_message}"
        )

        text = latest_message.lower()

        # ==================================================
        # MEMORY INSPECTION
        # ==================================================

        inspection_patterns = [

            "what do you remember about me",

            "what do you know about me",

            "list my memories",

            "list my preferences",

            "what are my preferences",

            "what do you know about this project",

            "what do you remember about this project"
        ]

        for pattern in inspection_patterns:

            if pattern in text:

                summary = (
                    build_memory_summary()
                )

                print(
                    "\n===== MEMORY INSPECTION ====="
                )

                print(summary)

                memory_text = (
                    "Known Memory Summary:\n\n"
                    + summary
                )

                llm_request.contents.insert(
                    0,
                    types.Content(
                        role="user",
                        parts=[
                            types.Part(
                                text=memory_text
                            )
                        ]
                    )
                )

                return None

        # ==================================================
        # NORMAL MEMORY RETRIEVAL
        # ==================================================

        memories = retrieve_relevant_memory(
            latest_message
        )

        print(
            f"[RETRIEVED] {memories}"
        )

        if not memories:
            return None

        memory_text = (
            "Known User Memory:\n\n"
            + "\n".join(memories)
        )

        print(
            f"[INJECTING]\n{memory_text}"
        )

        llm_request.contents.insert(
            0,
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text=memory_text
                    )
                ]
            )
        )

        return None

    except Exception as e:

        print(
            f"[RETRIEVAL ERROR] {e}"
        )

        return None
