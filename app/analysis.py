# Combines detection methods into a final decision
"""
analysis.py - Step 5: Analysis Layer
Combines perplexity and stylometric features for AI-generated text detection.
"""

from app.utils import calculate_perplexity
from app.text_processing import compute_stylometric_features, clean_text, tokenize_text

def analyze_text(text, tokenizer=None, model=None):
    """
    Analyze input text for potential AI generation.
    
    Parameters:
        text (str): The input text to analyze.
        tokenizer (optional): Language model tokenizer for perplexity.
        model (optional): Language model for perplexity.
        
    Returns:
        dict: Combined analysis results.
    """
    results = {}

    # 1️⃣ Clean and tokenize text
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    results['num_tokens'] = len(tokens)

    # 2️⃣ Perplexity analysis
    if tokenizer and model:
        try:
            ppl = calculate_perplexity(cleaned_text, tokenizer, model)
            results['perplexity'] = ppl
        except Exception as e:
            results['perplexity'] = None
            results['perplexity_error'] = str(e)
    else:
        results['perplexity'] = None
        results['perplexity_error'] = "Tokenizer/model not provided."

    # 3️⃣ Stylometric features
    try:
        stylometry = compute_stylometric_features(cleaned_text)
        results['stylometry'] = stylometry
    except Exception as e:
        results['stylometry'] = None
        results['stylometry_error'] = str(e)

    # 4️⃣ Detection decision (placeholder)
    # For now, just a simple heuristic: flag high perplexity or unusual stylometry
    results['ai_generated'] = None
    if results['perplexity'] and results['perplexity'] < 50:
        # Lower perplexity may indicate AI-generated text (example heuristic)
        results['ai_generated'] = True
    else:
        results['ai_generated'] = False

    return results


# Quick test when running this file directly
if __name__ == "__main__":
    sample_text = "This is a short test sentence to analyze."
    analysis = analyze_text(sample_text)
    print("Analysis results:")
    for k, v in analysis.items():
        print(f"{k}: {v}")
