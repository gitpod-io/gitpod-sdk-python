# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.subject import Subject
from .workflow_action_param import WorkflowActionParam
from .workflow_trigger_param import WorkflowTriggerParam
from .shared_params.codex_settings import CodexSettings

__all__ = ["AutomationCreateParams"]


class AutomationCreateParams(TypedDict, total=False):
    action: Required[WorkflowActionParam]
    """WorkflowAction defines the actions to be executed in a workflow."""

    codex_settings: Annotated[CodexSettings, PropertyInfo(alias="codexSettings")]
    """Codex app agent settings.

    Only meaningful when agent_id refers to the Codex app agent.
    """

    description: str
    """Description must be at most 500 characters:

    ```
    size(this) <= 500
    ```
    """

    executor: Optional[Subject]
    """Optional executor for the workflow.

    If not provided, defaults to the creator. Must be either the caller themselves
    or a service account.
    """

    name: str
    """Name must be between 1 and 80 characters:

    ```
    size(this) >= 1 && size(this) <= 80
    ```
    """

    report: WorkflowActionParam
    """WorkflowAction defines the actions to be executed in a workflow."""

    triggers: Iterable[WorkflowTriggerParam]
    """Automation must have between 1 and 10 triggers:

    ```
    size(this) >= 1 && size(this) <= 10
    ```
    """
