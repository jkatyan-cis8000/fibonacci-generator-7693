# Runtime layer for Fibonacci Generator
# App lifecycle, orchestration, wiring.

from ..service import fibonacci
from ..types import FibonacciNumber


def generate(max_value: int) -> list[FibonacciNumber]:
    """Generate Fibonacci numbers up to max_value.
    
    Args:
        max_value: Upper bound for generated Fibonacci numbers.
        
    Returns:
        List of Fibonacci numbers where each number <= max_value.
    """
    return fibonacci(max_value)
