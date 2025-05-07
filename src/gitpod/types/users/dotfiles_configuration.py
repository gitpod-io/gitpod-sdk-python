# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DotfilesConfiguration"]


class DotfilesConfiguration(BaseModel):
    repository: Optional[str] = None
    """The URL of a dotfiles repository."""
