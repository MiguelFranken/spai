import unittest
from unittest.mock import patch, mock_open
from transformers.website_a11y_report_transformer import transform_website_a11y_report


class TestTransformWebsiteA11yReport(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
            "accessibility_assessment": [
                {"id": "rule_1", "impact": "serious"},
                {"id": "rule_2", "impact": "critical"}
            ]
        }

    @patch(
        'builtins.open',
        new_callable=mock_open,
        read_data="rule_id,Why it Matters\nrule_1,Reason 1\nrule_2,Reason 2\n"
    )
    def test_transformer(self, mock_file):
        transformed_data = transform_website_a11y_report(self.mock_data)

        expected_output = {
            "a11y_extended": [
                {"rule_id": "rule_1", "impact": "serious", "why_it_matters": "Reason 1"},
                {"rule_id": "rule_2", "impact": "critical", "why_it_matters": "Reason 2"}
            ]
        }

        self.assertEqual(transformed_data, expected_output)


if __name__ == "__main__":
    unittest.main()
