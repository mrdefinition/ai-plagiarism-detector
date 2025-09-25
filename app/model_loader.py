# GPT-2 or other model loader
from transformers import GPT2Tokenizer, GPT2LMHeadModel

_tokenizer = None
_model = None

def load_model():
    """
    Loads GPT-2 tokenizer and model (cached).
    Returns:
        tokenizer, model
    """
    global _tokenizer, _model
    if _tokenizer is None or _model is None:
        _tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        _model = GPT2LMHeadModel.from_pretrained("gpt2")
        _model.eval()  # inference mode only
    return _tokenizer, _model


