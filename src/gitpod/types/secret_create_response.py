# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .secret import Secret
from .._models import BaseModel

__all__ = ["SecretCreateResponse"]


class SecretCreateResponse(BaseModel):
    secret: Optional[Secret] = None
