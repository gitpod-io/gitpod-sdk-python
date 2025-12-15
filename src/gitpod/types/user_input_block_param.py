# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserInputBlockParam", "Text"]


class Text(TypedDict, total=False):
    content: str


class UserInputBlockParam(TypedDict, total=False):
    text: Required[Text]

    id: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Timestamp when this block was created. Used for debugging and support bundles."""
