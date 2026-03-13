# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AutomationListExecutionOutputsResponse", "Values"]


class Values(BaseModel):
    bool_value: Optional[bool] = FieldInfo(alias="boolValue", default=None)

    float_value: Optional[float] = FieldInfo(alias="floatValue", default=None)

    int_value: Optional[str] = FieldInfo(alias="intValue", default=None)

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)


class AutomationListExecutionOutputsResponse(BaseModel):
    action_id: Optional[str] = FieldInfo(alias="actionId", default=None)

    values: Optional[Dict[str, Values]] = None
