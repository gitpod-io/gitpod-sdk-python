# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnterpriseAITokenUsage"]


class EnterpriseAITokenUsage(BaseModel):
    cache_tokens: Optional[str] = FieldInfo(alias="cacheTokens", default=None)

    input_tokens: Optional[str] = FieldInfo(alias="inputTokens", default=None)

    output_tokens: Optional[str] = FieldInfo(alias="outputTokens", default=None)

    total_tokens: Optional[str] = FieldInfo(alias="totalTokens", default=None)
