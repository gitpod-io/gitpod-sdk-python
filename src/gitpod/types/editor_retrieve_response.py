# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .editor import Editor
from .._models import BaseModel

__all__ = ["EditorRetrieveResponse"]


class EditorRetrieveResponse(BaseModel):
    editor: Optional[Editor] = None
    """editor contains the editor"""
