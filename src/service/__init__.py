# Service layer for Fibonacci Generator
# Business logic.

from src.types import FibonacciNumber


def fibonacci(max_value: int) -> list[FibonacciNumber]:
    """Generate Fibonacci numbers up to max_value.
    
    Args:
        max_value: Upper bound for generated Fibonacci numbers (inclusive).
        
    Returns:
        List of Fibonacci numbers where each number <= max_value.
        Returns empty list if max_value < 0.
    """
    if max_value < 0:
        return []
    
    if max_value == 0:
        return [0]
    
    result = [0, 1]
    while True:
        next_num = result[-1] + result[-2]
        if next_num > max_value:
            break
        result.append(next_num)
    
    return result
