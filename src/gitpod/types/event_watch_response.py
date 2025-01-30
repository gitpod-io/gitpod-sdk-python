# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EventWatchResponse"]


class EventWatchResponse(BaseModel):
    operation: Optional[
        Literal[
            "RESOURCE_OPERATION_UNSPECIFIED",
            "RESOURCE_OPERATION_CREATE",
            "RESOURCE_OPERATION_UPDATE",
            "RESOURCE_OPERATION_DELETE",
            "RESOURCE_OPERATION_UPDATE_STATUS",
        ]
    ] = None

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)

    resource_type: Optional[
        Literal[
            "RESOURCE_TYPE_UNSPECIFIED",
            "RESOURCE_TYPE_ENVIRONMENT",
            "RESOURCE_TYPE_RUNNER",
            "RESOURCE_TYPE_PROJECT",
            "RESOURCE_TYPE_TASK",
            "RESOURCE_TYPE_TASK_EXECUTION",
            "RESOURCE_TYPE_SERVICE",
            "RESOURCE_TYPE_ORGANIZATION",
            "RESOURCE_TYPE_USER",
            "RESOURCE_TYPE_ENVIRONMENT_CLASS",
            "RESOURCE_TYPE_RUNNER_SCM_INTEGRATION",
            "RESOURCE_TYPE_HOST_AUTHENTICATION_TOKEN",
            "RESOURCE_TYPE_GROUP",
            "RESOURCE_TYPE_PERSONAL_ACCESS_TOKEN",
            "RESOURCE_TYPE_USER_PREFERENCE",
            "RESOURCE_TYPE_SERVICE_ACCOUNT",
            "RESOURCE_TYPE_SECRET",
            "RESOURCE_TYPE_SSO_CONFIG",
        ]
    ] = FieldInfo(alias="resourceType", default=None)
