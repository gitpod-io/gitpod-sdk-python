# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .editor import Editor
from .._models import BaseModel

__all__ = ["EditorRetrieveResponse"]


class EditorRetrieveResponse(BaseModel):
    editor: Editor
    """editor contains the editor"""
