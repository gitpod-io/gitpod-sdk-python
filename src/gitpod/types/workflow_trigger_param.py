# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .workflow_trigger_context_param import WorkflowTriggerContextParam

__all__ = ["WorkflowTriggerParam", "PullRequest", "Time"]


class PullRequest(TypedDict, total=False):
    """
    Pull request trigger - executed when specified PR events occur.
     Only triggers for PRs in repositories matching the trigger context.
    """

    events: List[
        Literal[
            "PULL_REQUEST_EVENT_UNSPECIFIED",
            "PULL_REQUEST_EVENT_OPENED",
            "PULL_REQUEST_EVENT_UPDATED",
            "PULL_REQUEST_EVENT_APPROVED",
            "PULL_REQUEST_EVENT_MERGED",
            "PULL_REQUEST_EVENT_CLOSED",
            "PULL_REQUEST_EVENT_READY_FOR_REVIEW",
        ]
    ]

    integration_id: Annotated[Optional[str], PropertyInfo(alias="integrationId")]
    """
    integration_id is the optional ID of an integration that acts as the source of
    webhook events. When set, the trigger will be activated when the webhook
    receives events.
    """

    webhook_id: Annotated[Optional[str], PropertyInfo(alias="webhookId")]
    """
    webhook_id is the optional ID of a webhook that this trigger is bound to. When
    set, the trigger will be activated when the webhook receives events. This allows
    multiple workflows to share a single webhook endpoint.
    """


class Time(TypedDict, total=False):
    """
    Time-based trigger - executed automatically based on cron schedule.
     Uses standard cron expression format (minute hour day month weekday).
    """

    cron_expression: Annotated[str, PropertyInfo(alias="cronExpression")]
    """Cron expression must be between 1 and 100 characters:

    ```
    size(this) >= 1 && size(this) <= 100
    ```
    """


class WorkflowTriggerParam(TypedDict, total=False):
    """WorkflowTrigger defines when a workflow should be executed.

    Each trigger type defines a specific condition that will cause the workflow to execute:
    - Manual: Triggered explicitly by user action via StartWorkflow RPC
    - Time: Triggered automatically based on cron schedule
    - PullRequest: Triggered automatically when specified PR events occur

    Trigger Semantics:
    - Each trigger instance can create multiple workflow executions
    - Multiple triggers of the same workflow can fire simultaneously
    - Each trigger execution is independent and tracked separately
    - Triggers are evaluated in the context specified by WorkflowTriggerContext
    """

    context: Required[WorkflowTriggerContextParam]
    """WorkflowTriggerContext defines the context in which a workflow should run.

    Context determines where and how the workflow executes:

    - Projects: Execute in specific project environments
    - Repositories: Execute in environments created from repository URLs
    - Agent: Execute in agent-managed environments with custom prompts
    - FromTrigger: Use context derived from the trigger event (PR-specific)

    Context Usage by Trigger Type:

    - Manual: Can use any context type
    - Time: Typically uses Projects or Repositories context
    - PullRequest: Can use any context, FromTrigger uses PR repository context
    """

    manual: object
    """
    Manual trigger - executed when StartWorkflow RPC is called. No additional
    configuration needed.
    """

    pull_request: Annotated[PullRequest, PropertyInfo(alias="pullRequest")]
    """
    Pull request trigger - executed when specified PR events occur. Only triggers
    for PRs in repositories matching the trigger context.
    """

    time: Time
    """
    Time-based trigger - executed automatically based on cron schedule. Uses
    standard cron expression format (minute hour day month weekday).
    """
