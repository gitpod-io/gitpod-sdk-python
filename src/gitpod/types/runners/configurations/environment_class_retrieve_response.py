# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.environment_class import EnvironmentClass

__all__ = ["EnvironmentClassRetrieveResponse"]


class EnvironmentClassRetrieveResponse(BaseModel):
    environment_class: Optional[EnvironmentClass] = FieldInfo(alias="environmentClass", default=None)
