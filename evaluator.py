def evaluate_response(response: str) -> float:
    """
    Very simple scoring logic.
    Placeholder for real evaluation metrics.
    """
    score = len(response) / 100
    return min(score, 1.0)
