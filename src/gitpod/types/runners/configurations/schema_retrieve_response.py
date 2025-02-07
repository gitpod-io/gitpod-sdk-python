# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .runner_configuration_schema import RunnerConfigurationSchema

__all__ = ["SchemaRetrieveResponse"]


class SchemaRetrieveResponse(BaseModel):
    schema_: Optional[RunnerConfigurationSchema] = FieldInfo(alias="schema", default=None)
