"""A deliberately small Minecraft tick-time diagnostic utility."""


def average_mspt(samples):
    """Compute the mean time per tick (milliseconds)."""
    if not samples:
        raise ValueError("At least one tick sample is required")
    return sum(samples) / len(samples)


def overloaded(samples, budget_ms=50.0):
    """Return True if the *average* tick duration exceeds the budget."""
    return average_mspt(samples) > budget_ms
