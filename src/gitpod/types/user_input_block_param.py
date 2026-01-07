# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config

__all__ = ["UserInputBlockParam", "Image", "Text"]


class Image(TypedDict, total=False):
    """
    ImageInput allows sending images to the agent.
     Media type is inferred from magic bytes by the backend.
    """

    data: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Raw image data (max 4MB). Supported formats: PNG, JPEG, WebP."""


set_pydantic_config(Image, {"arbitrary_types_allowed": True})


class Text(TypedDict, total=False):
    content: str


class UserInputBlockParam(TypedDict, total=False):
    id: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Timestamp when this block was created. Used for debugging and support bundles."""

    image: Image
    """
    ImageInput allows sending images to the agent. Media type is inferred from magic
    bytes by the backend.
    """

    text: Text
