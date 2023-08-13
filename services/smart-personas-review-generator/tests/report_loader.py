import unittest
from unittest.mock import patch, mock_open

from data.report_loader import get_accessibility_violations

mock_file_content = """
{
    "context": "some_context",
    "report": [
        {"rule_id": "rule_1", "impact": "serious"},
        {"rule_id": "rule_2", "impact": "minor"},
        {"rule_id": "rule_3", "impact": "critical"}
    ]
}
"""


class TestGetAccessibilityViolations(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=mock_file_content)
    def test_default_impact_levels(self, mock_file):
        # Testing with default impact levels (serious, critical)
        file_path = 'dummy_file_path.json'
        violations = get_accessibility_violations(file_path)

        expected_output = [
            {"rule_id": "rule_1", "impact": "serious"},
            {"rule_id": "rule_3", "impact": "critical"}
        ]

        self.assertEqual(violations, expected_output)

    @patch('builtins.open', new_callable=mock_open, read_data=mock_file_content)
    def test_custom_impact_levels(self, mock_file):
        # Testing with a custom impact level (minor)
        file_path = 'dummy_file_path.json'
        violations = get_accessibility_violations(file_path, impact_levels=['minor'])

        expected_output = [
            {"rule_id": "rule_2", "impact": "minor"}
        ]

        self.assertEqual(violations, expected_output)


if __name__ == "__main__":
    unittest.main()
