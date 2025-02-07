# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["Principal"]

Principal: TypeAlias = Literal[
    "PRINCIPAL_UNSPECIFIED",
    "PRINCIPAL_ACCOUNT",
    "PRINCIPAL_USER",
    "PRINCIPAL_RUNNER",
    "PRINCIPAL_ENVIRONMENT",
    "PRINCIPAL_SERVICE_ACCOUNT",
]
