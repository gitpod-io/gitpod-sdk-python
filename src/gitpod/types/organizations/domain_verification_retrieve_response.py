# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .domain_verification import DomainVerification

__all__ = ["DomainVerificationRetrieveResponse"]


class DomainVerificationRetrieveResponse(BaseModel):
    domain_verification: DomainVerification = FieldInfo(alias="domainVerification")
