def format_violations(json_data):
    violations_string = ""

    for violation in json_data:
        violations_string += f"Violation ID: {violation['id']}\n"
        violations_string += f"Description: {violation['description']}\n"
        violations_string += f"Help: {violation['help']}\n"
        violations_string += f"Impact: {violation['impact']}\n\n"

    return violations_string
