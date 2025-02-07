# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .field_validation_error import FieldValidationError

__all__ = ["EnvironmentClassValidationResult"]


class EnvironmentClassValidationResult(BaseModel):
    configuration_errors: Optional[List[FieldValidationError]] = FieldInfo(alias="configurationErrors", default=None)

    description_error: Optional[str] = FieldInfo(alias="descriptionError", default=None)

    display_name_error: Optional[str] = FieldInfo(alias="displayNameError", default=None)

    valid: Optional[bool] = None
