# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IdentityExchangeTokenParams"]


class IdentityExchangeTokenParams(TypedDict, total=False):
    exchange_token: Annotated[str, PropertyInfo(alias="exchangeToken")]
    """exchange_token is the token to exchange"""
