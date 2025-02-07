# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LoginProvider"]


class LoginProvider(BaseModel):
    login_url: Optional[str] = FieldInfo(alias="loginUrl", default=None)
    """login_url is the URL to redirect the browser agent to for login"""

    provider: Optional[str] = None
    """provider is the provider used by this login method, e.g.

    "github", "google", "custom"
    """
