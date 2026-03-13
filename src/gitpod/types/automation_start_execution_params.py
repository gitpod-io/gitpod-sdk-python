# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .workflow_trigger_context_param import WorkflowTriggerContextParam

__all__ = ["AutomationStartExecutionParams"]


class AutomationStartExecutionParams(TypedDict, total=False):
    context_override: Annotated[Optional[WorkflowTriggerContextParam], PropertyInfo(alias="contextOverride")]
    """
    Optional context override for the execution. When provided, replaces the
    workflow's default trigger context. User must have appropriate permissions on
    the overridden resources. Supports Projects, Repositories, and Agent context
    types. FromTrigger context type is not supported for manual overrides.
    """

    parameters: Dict[str, str]
    """
    Parameters to substitute into workflow steps using Go template syntax. Use
    {{ .Parameters.key_name }} in templatable fields (task.command, agent.prompt,
    pull*request.title/description/branch, trigger context agent.prompt). Keys must
    match pattern ^[a-zA-Z*][a-zA-Z0-9_]\\**$ Maximum 10 parameters allowed. Empty map
    is treated as no parameters provided.
    """

    workflow_id: Annotated[str, PropertyInfo(alias="workflowId")]
