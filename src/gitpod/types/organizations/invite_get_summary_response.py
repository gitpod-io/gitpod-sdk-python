# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InviteGetSummaryResponse"]


class InviteGetSummaryResponse(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")

    organization_member_count: Optional[int] = FieldInfo(alias="organizationMemberCount", default=None)

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)
