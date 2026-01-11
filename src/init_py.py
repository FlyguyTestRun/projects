"""
==============================================================================
Application Package Initialization
==============================================================================
Location: src/__init__.py
Purpose: Initialize the application package and expose public API
==============================================================================
"""

# Version information
__version__ = "0.1.0"
__author__ = "Your Team Name"
__license__ = "MIT"

# Package metadata
__all__ = [
    "create_app",
    "get_version",
]


def get_version() -> str:
    """
    Get the current application version.
    
    Returns:
        str: Version string (e.g., "0.1.0")
    
    Example:
        >>> from src import get_version
        >>> print(get_version())
        0.1.0
    """
    return __version__


def create_app():
    """
    Application factory function.
    
    Creates and configures the application instance.
    This pattern allows for easier testing and multiple configurations.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    
    Example:
        >>> from src import create_app
        >>> app = create_app()
        >>> # Use with uvicorn
        >>> # uvicorn src:create_app --factory
    """
    from src.main import app
    return app


# ==============================================================================
# NOTES FOR STUDENTS
# ==============================================================================
#
# __init__.py Purpose:
# - Marks directory as a Python package
# - Can contain package initialization code
# - Defines what gets imported with "from package import *"
#
# Best Practices:
# 1. Keep it minimal - don't put business logic here
# 2. Use __all__ to explicitly define public API
# 3. Version info helps with debugging
# 4. Factory pattern (create_app) is better than globals
#
# Common Patterns:
# - Import submodules to make them accessible
# - Initialize loggers or configurations
# - Expose commonly used functions/classes
#
# ==============================================================================
