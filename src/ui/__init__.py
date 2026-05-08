# UI layer for Fibonacci Generator
# User-facing surfaces — CLI, web, GUI.

from ..service import fibonacci
from ..types import FibonacciNumber
from ..config import parse_input
import sys


def parse_args(args: list[str]) -> int:
    """Parse command line arguments.
    
    Args:
        args: List of command line argument strings.
        
    Returns:
        Integer max value for Fibonacci generation.
        
    Raises:
        ValueError: If arguments are invalid or missing.
    """
    if not args:
        raise ValueError("Missing max value argument")
    return parse_input(args[0])


def display_results(numbers: list[FibonacciNumber]) -> None:
    """Print Fibonacci results to stdout.
    
    Args:
        numbers: List of Fibonacci numbers to display.
    """
    print(" ".join(str(n) for n in numbers))


def main() -> int:
    """CLI entry point."""
    try:
        max_value = parse_args(sys.argv[1:])
        numbers = fibonacci(max_value)
        display_results(numbers)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
