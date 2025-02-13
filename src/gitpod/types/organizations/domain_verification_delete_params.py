# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DomainVerificationDeleteParams"]


class DomainVerificationDeleteParams(TypedDict, total=False):
    domain_verification_id: Required[Annotated[str, PropertyInfo(alias="domainVerificationId")]]
