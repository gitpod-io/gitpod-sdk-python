# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["EditorResolveURLResponse"]


class EditorResolveURLResponse(BaseModel):
    url: str
    """url is the resolved editor URL"""
