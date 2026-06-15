from functools import wraps
import time


def safe_tool(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        try:
            print(f"[TOOL START] {func.__name__}")
            print(f"[ARGS] {args} {kwargs}")

            result = func(*args, **kwargs)

            duration = round(time.time() - start, 2)

            print(f"[TOOL SUCCESS] {func.__name__}")
            print(f"[TIME] {duration}s")

            return result

        except Exception as e:

            duration = round(time.time() - start, 2)

            print(f"[TOOL ERROR] {func.__name__}")
            print(f"[TIME] {duration}s")
            print(f"[ERROR] {str(e)}")

            return f"Tool Error: {str(e)}"

    return wrapper
