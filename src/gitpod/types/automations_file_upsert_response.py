# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AutomationsFileUpsertResponse"]


class AutomationsFileUpsertResponse(BaseModel):
    updated_service_ids: Optional[List[str]] = FieldInfo(alias="updatedServiceIds", default=None)

    updated_task_ids: Optional[List[str]] = FieldInfo(alias="updatedTaskIds", default=None)
