import os
import json
from config import REPORTS_DIR


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def get_website_context(file_path):
    json_data = load_json_data(file_path)
    return json_data['context']


def get_accessibility_violations(file_path, impact_levels=None):
    """
    Returns a list of accessibility violations from the JSON report file located at `file_path`.
    If `impact_levels` is not provided, the function will return violations with 'serious' and 'critical' impact levels.

    Args:
        file_path (str): The path to the JSON report file.
        impact_levels (list, optional): A list of impact levels to filter violations by. Defaults to ['serious', 'critical'].

    Returns:
        list: A list of accessibility violations with the specified impact levels.
    """
    if impact_levels is None:
        impact_levels = ['serious', 'critical']
    json_data = load_json_data(file_path)
    return [entry for entry in json_data['report'] if entry['impact'] in impact_levels]


def get_all_report_files(directory=REPORTS_DIR):
    """
    Returns a list of all JSON report files in the specified directory.

    Args:
        directory (str, optional): The directory to search for report files. Defaults to REPORTS_DIR.

    Returns:
        list: A list of file paths for all JSON report files in the specified directory.
    """
    return [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(".json")]
