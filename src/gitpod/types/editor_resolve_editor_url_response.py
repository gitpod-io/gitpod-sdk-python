# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EditorResolveEditorURLResponse"]


class EditorResolveEditorURLResponse(BaseModel):
    url: Optional[str] = None
    """url is the resolved editor URL"""
