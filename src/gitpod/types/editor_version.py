# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EditorVersion"]


class EditorVersion(BaseModel):
    version: str
    """version is the version string of the editor Examples for JetBrains: 2025.2"""
