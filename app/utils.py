# Utility functions (perplexity, helpers)
import torch

def calculate_perplexity(text, tokenizer, model):
    """
    Calculates perplexity of a text using a language model.
    
    Args:
        text (str): Input text to evaluate
        tokenizer: HuggingFace tokenizer
        model: HuggingFace LM (e.g., GPT-2)
    
    Returns:
        float: Perplexity score
    """
    if not text.strip():
        return float("inf")  # meaningless for empty text

    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(inputs, labels=inputs)
        loss = outputs.loss
    return torch.exp(loss).item()
