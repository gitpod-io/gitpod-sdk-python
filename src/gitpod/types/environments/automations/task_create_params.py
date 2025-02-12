# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.task_spec import TaskSpec
from ...shared_params.task_metadata import TaskMetadata

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    depends_on: Annotated[List[str], PropertyInfo(alias="dependsOn")]

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    metadata: TaskMetadata

    spec: TaskSpec
