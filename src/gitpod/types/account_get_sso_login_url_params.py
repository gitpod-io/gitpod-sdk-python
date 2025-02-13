# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountGetSSOLoginURLParams"]


class AccountGetSSOLoginURLParams(TypedDict, total=False):
    email: Required[str]
    """email is the email the user wants to login with"""

    return_to: Annotated[Optional[str], PropertyInfo(alias="returnTo")]
    """return_to is the URL the user will be redirected to after login"""
