#!/usr/bin/env python3
"""Linter for the Fibonacci Generator project.

Enforces:
- Files live in exactly one layer directory under src/
- Imports respect the forward dependency direction
- No file exceeds 300 lines
"""

import ast
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent / "src"

# Layer dependency rules: each layer may only import from these layers
ALLOWED_IMPORTS = {
    "types": {"types"},
    "config": {"types", "config"},
    "utils": {"utils"},
    "providers": {"types", "config", "utils", "providers"},
    "repo": {"types", "config", "repo"},
    "service": {"types", "config", "repo", "providers", "service"},
    "runtime": {"types", "config", "repo", "service", "providers", "runtime"},
    "ui": {"types", "config", "service", "runtime", "providers", "ui"},
}

LAYER_DIRS = set(ALLOWED_IMPORTS.keys())


def get_layer(filepath: Path) -> str | None:
    """Return the layer name for a file, or None if not in src/."""
    try:
        rel_path = filepath.relative_to(SRC_DIR)
        parts = rel_path.parts
        if parts and parts[0] in LAYER_DIRS:
            return parts[0]
    except ValueError:
        pass
    return None


def get_imports(filepath: Path) -> list[tuple[str, int]]:
    """Return list of (module_name, line_number) for imports in the file."""
    imports = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        tree = ast.parse(content, filename=str(filepath))

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append((alias.name, node.lineno))
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append((node.module, node.lineno))
    except SyntaxError:
        pass
    return imports


def check_line_count(filepath: Path) -> list[str]:
    """Check if file exceeds 300 lines."""
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if len(lines) > 300:
        errors.append(f"{filepath}: exceeds 300 lines ({len(lines)} lines)")
    return errors


def check_imports(filepath: Path) -> list[str]:
    """Check that imports respect layer dependency rules."""
    errors = []
    layer = get_layer(filepath)
    if layer is None:
        return errors

    allowed = ALLOWED_IMPORTS.get(layer, set())
    imports = get_imports(filepath)

    for module_name, lineno in imports:
        # Check if module is in src/ and belongs to a layer
        module_path = SRC_DIR / module_name.replace(".", "/")
        if module_path.exists() or (module_path.parent / "__init__.py").exists():
            # This is an internal import - check layer
            for import_part in module_name.split("."):
                import_layer = SRC_DIR / import_part
                if import_layer.exists() and import_part in LAYER_DIRS:
                    if import_part not in allowed:
                        errors.append(
                            f"{filepath}:{lineno}: import '{module_name}' "
                            f"from disallowed layer '{import_part}' (layer '{layer}' may only import from {sorted(allowed)})"
                        )
                    break

    return errors


def check_file(filepath: Path) -> list[str]:
    """Run all checks on a single file."""
    errors = []
    errors.extend(check_line_count(filepath))
    errors.extend(check_imports(filepath))
    return errors


def main() -> int:
    """Run linter on all Python files under src/."""
    errors = []

    for py_file in SRC_DIR.rglob("*.py"):
        # Skip __pycache__ directories
        if "__pycache__" in py_file.parts:
            continue
        errors.extend(check_file(py_file))

    if errors:
        print("Lint errors found:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
