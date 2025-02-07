# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["HostAuthenticationTokenSource"]

HostAuthenticationTokenSource: TypeAlias = Literal[
    "HOST_AUTHENTICATION_TOKEN_SOURCE_UNSPECIFIED",
    "HOST_AUTHENTICATION_TOKEN_SOURCE_OAUTH",
    "HOST_AUTHENTICATION_TOKEN_SOURCE_PAT",
]
