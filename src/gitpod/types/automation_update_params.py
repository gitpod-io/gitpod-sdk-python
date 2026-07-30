# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.subject import Subject
from .workflow_action_param import WorkflowActionParam
from .workflow_trigger_param import WorkflowTriggerParam
from .shared_params.codex_settings import CodexSettings

__all__ = ["AutomationUpdateParams"]


class AutomationUpdateParams(TypedDict, total=False):
    action: Optional[WorkflowActionParam]
    """WorkflowAction defines the actions to be executed in a workflow."""

    codex_settings: Annotated[Optional[CodexSettings], PropertyInfo(alias="codexSettings")]
    """Codex app agent settings.

    Only meaningful when agent_id refers to the Codex app agent.
    """

    description: Optional[str]
    """Description must be at most 500 characters:

    ```
    size(this) <= 500
    ```
    """

    disabled: Optional[bool]
    """When set, enables or disables the workflow.

    A disabled workflow will not be triggered by any automatic trigger and manual
    starts are rejected.
    """

    executor: Optional[Subject]

    name: Optional[str]
    """Name must be between 1 and 80 characters:

    ```
    size(this) >= 1 && size(this) <= 80
    ```
    """

    report: Optional[WorkflowActionParam]
    """WorkflowAction defines the actions to be executed in a workflow."""

    triggers: Iterable[WorkflowTriggerParam]
    """Automation can have at most 10 triggers:

    ```
    size(this) <= 10
    ```
    """

    workflow_id: Annotated[str, PropertyInfo(alias="workflowId")]
