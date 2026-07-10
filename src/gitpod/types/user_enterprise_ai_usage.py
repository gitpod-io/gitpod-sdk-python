# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .enterprise_ai_usage import EnterpriseAIUsage

__all__ = ["UserEnterpriseAIUsage"]


class UserEnterpriseAIUsage(BaseModel):
    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    usage: Optional[EnterpriseAIUsage] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Empty when representing the "Others" aggregation bucket."""
