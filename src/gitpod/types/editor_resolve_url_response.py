# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EditorResolveURLResponse"]


class EditorResolveURLResponse(BaseModel):
    url: Optional[str] = None
    """url is the resolved editor URL"""
