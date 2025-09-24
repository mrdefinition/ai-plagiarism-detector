def test_placeholder():
    assert True
from app.model_loader import load_model

def test_model_loader_loads():
    tokenizer, model = load_model()
    assert tokenizer is not None
    assert model is not None

