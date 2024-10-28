# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerInteractionGetHostAuthenticationTokenValueResponse"]


class RunnerInteractionGetHostAuthenticationTokenValueResponse(BaseModel):
    token_id: Optional[str] = FieldInfo(alias="tokenId", default=None)
    """The host authentication token's ID"""

    value: Optional[str] = None
    """
    The authentication token encrypted as NaCL anonymous sealed box using the
    runner's public key.
    """
