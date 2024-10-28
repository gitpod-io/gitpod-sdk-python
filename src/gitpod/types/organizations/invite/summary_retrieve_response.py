# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SummaryRetrieveResponse"]


class SummaryRetrieveResponse(BaseModel):
    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    organization_member_count: Optional[int] = FieldInfo(alias="organizationMemberCount", default=None)

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)
