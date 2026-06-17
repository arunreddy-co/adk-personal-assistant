async def retrieval_callback(
    callback_context,
    llm_request
):

    print("\n===== RETRIEVAL CALLBACK =====")

    print(type(callback_context))
    print(type(llm_request))

    print("\n===== REQUEST =====")

    print(llm_request)

    return None
