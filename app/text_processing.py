import re
import string
import nltk
from collections import Counter

# Ensure NLTK resources are available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)


def clean_text(text: str) -> str:
    """
    Basic cleaning: lowercase, remove extra spaces, strip non-printables.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = "".join(ch for ch in text if ch in string.printable)
    return text.strip()


def tokenize_text(text: str):
    """
    Tokenize into words using NLTK.
    """
    return nltk.word_tokenize(text)


def compute_stylometric_features(text: str) -> dict:
    """
    Compute simple stylometric features for text.
    
    Returns:
        dict with metrics (avg sentence length, vocab richness, punctuation ratio)
    """
    if not text.strip():
        return {
            "avg_sentence_length": 0,
            "vocab_richness": 0,
            "punctuation_ratio": 0
        }

    # Sentences & words
    sentences = nltk.sent_tokenize(text)
    words = tokenize_text(text)
    
    # Metrics
    avg_sentence_length = sum(len(s.split()) for s in sentences) / max(1, len(sentences))
    vocab_richness = len(set(words)) / max(1, len(words))
    punctuation_count = sum(ch in string.punctuation for ch in text)
    punctuation_ratio = punctuation_count / max(1, len(text))
    
    return {
        "avg_sentence_length": round(avg_sentence_length, 3),
        "vocab_richness": round(vocab_richness, 3),
        "punctuation_ratio": round(punctuation_ratio, 3),
    }
