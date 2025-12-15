# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SecretRef"]


class SecretRef(BaseModel):
    """SecretRef references a secret by its ID."""

    id: Optional[str] = None
    """id is the UUID of the secret to reference."""
