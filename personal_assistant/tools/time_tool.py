from datetime import datetime
from zoneinfo import ZoneInfo

from personal_assistant.tools.tool_base import safe_tool


@safe_tool
def get_current_time(
    timezone: str = "Asia/Kolkata"
):
    return datetime.now(
        ZoneInfo(timezone)
    ).strftime("%Y-%m-%d %H:%M:%S")
