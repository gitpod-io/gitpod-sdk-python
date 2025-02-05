# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountGetSSOLoginURLParams"]


class AccountGetSSOLoginURLParams(TypedDict, total=False):
    return_to: Required[Annotated[str, PropertyInfo(alias="returnTo")]]
    """return_to is the URL the user will be redirected to after login"""

    email: str
    """email is the email the user wants to login with"""
