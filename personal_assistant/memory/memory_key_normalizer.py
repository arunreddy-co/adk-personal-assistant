KEY_MAP = {

    "preferred_editor":
        "favorite_editor",

    "editor_preference":
        "favorite_editor",

    "project_phase":
        "current_phase",

    "project_title":
        "project_name",

}

def normalize_memory_key(
    key: str
):

    if not key:
        return key

    return KEY_MAP.get(
        key,
        key
    )
