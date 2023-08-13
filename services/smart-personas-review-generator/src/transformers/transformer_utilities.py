import re


def clean(input_data) -> [str, dict]:
    """
    Cleans input data by removing extra whitespace and newlines.

    Args:
        input_data: A string or dictionary to be cleaned.

    Returns:
        If input_data is a string, returns the cleaned string.
        If input_data is a dictionary, returns a new dictionary with cleaned string values.

    Raises:
        TypeError: If input_data is not a string or dictionary.
    """
    if isinstance(input_data, str):
        tmp = re.sub(r'(\r\n|\r|\n){2,}', r'\n', input_data)
        return re.sub(r'[ \t]+', ' ', tmp)
    elif isinstance(input_data, dict):
        cleaned_data = {}
        for key, value in input_data.items():
            if isinstance(value, str):  # Ensure we only clean string values in the dictionary
                cleaned_data[key] = clean(value)  # Recursively call the cleaning function
            else:
                cleaned_data[key] = value  # Retain non-string values as they are
        return cleaned_data
    else:
        # Raise an error for unsupported types or handle as you see fit
        raise TypeError("Only strings or dictionaries are supported.")

