from app.text_processing import clean_text, tokenize_text, compute_stylometric_features

def test_clean_text_removes_spaces_and_lowercases():
    raw = "Hello   WORLD!!!\n"
    cleaned = clean_text(raw)
    assert "world" in cleaned
    assert "\n" not in cleaned

def test_tokenize_text():
    tokens = tokenize_text("This is a test.")
    assert "This" in tokens or "this" in tokens
    assert isinstance(tokens, list)

def test_compute_stylometric_features():
    text = "This is a sentence. Here is another one!"
    features = compute_stylometric_features(text)
    assert "avg_sentence_length" in features
    assert "vocab_richness" in features
    assert "punctuation_ratio" in features
    assert features["avg_sentence_length"] > 0
