
def transform_website_context(inputs: dict) -> dict:
    """
    Transforms website context to extract necessary metadata.

    Args:
        inputs (dict): Input dictionary containing the website description.

    Returns:
        dict: Dictionary with extracted website metadata.
    """
    website_context = inputs["website_description"]
    # Always map these keys
    transformed = {
        "website_metadata_url": website_context.get("url", ""),
        "website_metadata_title": website_context.get("title", ""),
        "website_metadata_description": website_context.get("description", "")
    }

    # Collect metadata for other keys in the input dictionary
    metadata = {}
    for key, value in website_context.items():
        # Skip the keys that we've already mapped
        if key not in ["url", "title", "description"]:
            metadata[key] = value

    # Assign the metadata dictionary to the transformed dictionary
    transformed["website_metadata"] = metadata

    return transformed
