# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .scm_integration_validation_result import ScmIntegrationValidationResult
from .environment_class_validation_result import EnvironmentClassValidationResult

__all__ = ["ConfigurationValidateResponse"]


class ConfigurationValidateResponse(BaseModel):
    environment_class: Optional[EnvironmentClassValidationResult] = FieldInfo(alias="environmentClass", default=None)

    scm_integration: Optional[ScmIntegrationValidationResult] = FieldInfo(alias="scmIntegration", default=None)
