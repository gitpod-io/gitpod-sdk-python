# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SecretRef"]


class SecretRef(TypedDict, total=False):
    """SecretRef references a secret by its ID."""

    id: str
    """id is the UUID of the secret to reference."""
