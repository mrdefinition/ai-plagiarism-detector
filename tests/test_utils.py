import sys, os
# Add the project root (A.I.P) to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
def test_placeholder():
    assert True
from app.utils import calculate_perplexity
from app.model_loader import load_model

def test_perplexity_runs():
    tokenizer, model = load_model()
    text = "This is a short test sentence."
    ppl = calculate_perplexity(text, tokenizer, model)
    assert isinstance(ppl, float)
    assert ppl > 0
