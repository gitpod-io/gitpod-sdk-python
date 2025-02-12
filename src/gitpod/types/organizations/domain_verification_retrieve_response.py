# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .domain_verification import DomainVerification

__all__ = ["DomainVerificationRetrieveResponse"]


class DomainVerificationRetrieveResponse(BaseModel):
    domain_verification: Optional[DomainVerification] = FieldInfo(alias="domainVerification", default=None)
