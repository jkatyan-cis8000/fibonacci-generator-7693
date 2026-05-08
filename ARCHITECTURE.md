# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/types/__init__.py: FibonacciNumber type alias for integer sequences
- src/config/__init__.py: Configuration constants (max value, default limit)
- src/service/__init__.py: fibonacci(max_value: int) -> list[FibonacciNumber] - core business logic
- src/ui/__init__.py: CLI interface - parse command line args, display results
- src/runtime/__init__.py: Application entry point - wire services and run
- src/utils/__init__.py: Utility functions (input validation helpers)

## Interfaces

### service module
- `fibonacci(max_value: int) -> list[int]`: Generate Fibonacci numbers up to max_value
  - Returns list of Fibonacci numbers where each number <= max_value
  - Validates input is non-negative
  - Returns empty list if max_value < 0

### ui module
- `parse_args(args: list[str]) -> int`: Parse command line arguments
  - Expects single integer argument for max value
  - Raises ValueError if argument is invalid
- `display_results(numbers: list[int]) -> None`: Print results to stdout
  - Formats output for readability

### runtime module
- `main() -> int`: Entry point
  - Returns exit code (0 for success, 1 for error)

## Shared Data Structures

- `FibonacciNumber = int`: Type alias for Fibonacci sequence values
- `max_value: int`: Upper bound for generated Fibonacci numbers (exclusive upper bound)

## External Dependencies

None required. Uses only Python standard library.
