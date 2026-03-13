# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AutomationDeleteParams"]


class AutomationDeleteParams(TypedDict, total=False):
    force: bool
    """
    force indicates whether to immediately delete the workflow and all related
    resources. When true, performs cascading deletion of:

    - All workflow executions
    - All workflow execution actions
    - All environments created by workflow actions
    - All agent executions created by workflow actions
    - The workflow itself When false (default), marks workflow executions for
      deletion and relies on background reconciliation to clean up resources.
    """

    workflow_id: Annotated[str, PropertyInfo(alias="workflowId")]
