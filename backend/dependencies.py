"""Dependencies module for OmniBrain API.

This module prepares for future FastAPI dependency injections.
"""

def get_settings():
    """Dependency injection provider for application settings."""
    from backend.config import settings
    return settings
