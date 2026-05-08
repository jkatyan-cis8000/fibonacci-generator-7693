# Config layer for Fibonacci Generator
# Configuration constants.

# Configuration constants
DEFAULT_MAX_VALUE = 100
MAX_LINE_LENGTH = 300


def parse_input(value_str: str) -> int:
    """Parse string input to integer.
    
    Args:
        value_str: String representation of an integer.
        
    Returns:
        Integer value.
        
    Raises:
        ValueError: If the string is not a valid integer.
    """
    return int(value_str)
