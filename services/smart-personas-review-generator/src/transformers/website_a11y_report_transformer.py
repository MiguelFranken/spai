import csv


def transform_website_a11y_report(inputs: dict) -> dict:
    """
    Transforms website accessibility report.

    Args:
        inputs (dict): Input dictionary containing the accessibility assessment.

    Returns:
        dict: Dictionary with extended accessibility violations.
    """
    a11y_report = inputs["accessibility_assessment"]
    rule_id_to_why_it_matters = get_why_it_matters_from_csv('data/a11y_rules.csv')

    violations_extended = []

    for violation in a11y_report:
        rule_id = violation['id']
        why_it_matters = rule_id_to_why_it_matters.get(rule_id, "Unknown Reason")
        extended_violation = {
            "rule_id": rule_id,
            "impact": violation['impact'],
            "why_it_matters": why_it_matters,
        }
        violations_extended.append(extended_violation)

    return {
        "a11y_extended": violations_extended
    }


def get_why_it_matters_from_csv(file_path: str) -> dict:
    """
    Reads the "Why it Matters" details from the given CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: Dictionary mapping from rule_id to its description.
    """
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rule_id_to_why_it_matters = {}
        for row in csv_reader:
            rule_id_to_why_it_matters[row['rule_id']] = row['Why it Matters']
    return rule_id_to_why_it_matters
