from transformers.transformer_utilities import clean


def get_possessive_form(name):
    """
    Returns the possessive form of a given name.

    Args:
        name (str): The name to transform.

    Returns:
        str: The possessive form of the given name.
    """
    if name.endswith('s'):
        return f"{name}'"
    else:
        return f"{name}'s"


def transform_name(inputs: dict) -> dict:
    """
    Transforms inputs to get persona name and its possessive form.

    Args:
        inputs (dict): Input dictionary containing the cleaned persona details.

    Returns:
        dict: Dictionary with persona name and its possessive form.
    """
    return {
        "persona_name": inputs["clean_persona"]["name"],
        "persona_name_possessive": get_possessive_form(inputs["clean_persona"]["name"])
    }


def transform_story(inputs: dict) -> dict:
    """
    Transforms inputs to get persona story.

    Args:
        inputs (dict): Input dictionary containing the cleaned persona details.

    Returns:
        dict: Dictionary with persona story.
    """
    return {
        "persona_story": inputs["clean_persona"]["story"]
    }


def transform_clean(inputs: dict) -> dict:
    return {
        "clean_persona": clean(inputs["persona"]),
    }
