# Utils layer for Fibonacci Generator
# Pure helpers; no domain logic, no internal imports.


def parse_max_value(string: str) -> int:
    """Parse a string into a max value for Fibonacci generation.
    
    Args:
        string: String representation of the max value.
        
    Returns:
        Integer max value.
        
    Raises:
        ValueError: If the string cannot be parsed as an integer.
    """
    try:
        return int(string)
    except ValueError:
        raise ValueError(f"Invalid max value: {string}")
