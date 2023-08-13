from textblob import TextBlob
import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize


# Downloading datasets from nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')

# Pre-defined list of known technical terms
KNOWN_TECH_TERMS = ["HTML", "CSS", "JavaScript", "accessibility", ...]


def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.33:
        return polarity, "positive"
    elif polarity < 0.1:
        return polarity, "negative"
    else:
        return polarity, "neutral"


def detect_technical_terms(text):
    """Detect technical terms in the provided text."""
    words_in_text = word_tokenize(text)
    tagged = nltk.pos_tag(words_in_text)

    uncommon_nouns = [word for word, pos in tagged if (pos == "NN" and word.lower() not in words.words())]
    known_terms_detected = [term for term in KNOWN_TECH_TERMS if term in words_in_text]

    return set(known_terms_detected)


def calculate_metrics(response):
    """Calculate the required metrics for the provided response."""
    metrics = {}
    paragraphs = response.split("\n\n")
    metrics["num_paragraphs"] = len(paragraphs)
    metrics["text_length"] = len(response)

    polarity, sentiment_label = get_sentiment(response)
    metrics['sentiment_polarity'] = polarity
    metrics['sentiment'] = sentiment_label

    tech_terms = detect_technical_terms(response)
    metrics["technical_terms"] = ", ".join(tech_terms)

    return metrics
