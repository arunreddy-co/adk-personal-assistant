CATEGORY_MAP = {

    # Occupation

    "user_role":
        "occupation",

    "user_profession":
        "occupation",

    "profession":
        "occupation",

    "job":
        "occupation",

    "status":
	"occupation",

    # Location

    "residence":
        "location",

    "city":
        "location",

    "home_location":
        "location",

    # Learning

    "learning_activity":
        "learning_topic",

    "learning_programming_language":
        "learning_topic",

    "studying":
        "learning_topic",

    # Editor

    "editor_preference":
        "favorite_editor",

    "preferred_editor":
        "favorite_editor",

    "preferred_text_editor":
        "favorite_editor",
}


def normalize_category(
    category: str
):

    if not category:
        return category

    return CATEGORY_MAP.get(
        category,
        category
    )
