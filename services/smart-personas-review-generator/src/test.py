from review_generator import ReviewGenerator
from config import PERSONA_NAME, MAX_REPORTS_TO_PROCESS, PARAGRAPH_LIMIT
from data import report_loader
from data.personal_info_factory import PersonalInfoFactory
import pandas as pd
import time
from metrics import calculate_metrics


def generate_responses():
    generator = ReviewGenerator()
    report_files = report_loader.get_all_report_files()
    all_responses = []

    print(f"Found {len(report_files)} reports.")

    for idx, report_file in enumerate(report_files):
        if idx >= MAX_REPORTS_TO_PROCESS:
            break

        context = report_loader.get_website_context(report_file)
        violations = report_loader.get_accessibility_violations(report_file)
        persona = PersonalInfoFactory.get_persona(PERSONA_NAME)

        start_time = time.time()
        response_text = generator.generate(context, violations, persona, PARAGRAPH_LIMIT)
        end_time = time.time()
        computation_time = end_time - start_time

        metrics = calculate_metrics(response_text)
        metrics["computation_time"] = computation_time

        all_responses.append({
            'Report File': report_file,
            'Context': context,
            'Violations': violations,
            'Persona': persona,
            'Response': response_text,
            "Number of Paragraphs": metrics["num_paragraphs"],
            "Text Length": metrics["text_length"],
            "Technical Terms": metrics["technical_terms"],
            "Computation Time": metrics["computation_time"],
            "Sentiment": metrics["sentiment"],
            "Sentiment Polarity": metrics["sentiment_polarity"]
        })

    return all_responses


def save_responses_to_csv(responses):
    df = pd.DataFrame(responses)
    df.to_csv("../out/results.csv", index=False)


def main():
    print("Generating test reponses for reports.")
    responses = generate_responses()
    print(f'Processed {len(responses)} report(s).')
    save_responses_to_csv(responses)


if __name__ == "__main__":
    main()
