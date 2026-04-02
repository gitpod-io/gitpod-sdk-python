# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkflowStepParam", "Agent", "PullRequest", "Task"]


class Agent(TypedDict, total=False):
    """WorkflowAgentStep represents an agent step that executes with a prompt."""

    prompt: str
    """Prompt must be between 1 and 20,000 characters:

    ```
    size(this) >= 1 && size(this) <= 20000
    ```
    """


class PullRequest(TypedDict, total=False):
    """WorkflowPullRequestStep represents a pull request creation step."""

    branch: str
    """Branch name must be between 1 and 255 characters:

    ```
    size(this) >= 1 && size(this) <= 255
    ```
    """

    description: str
    """Description must be at most 20,000 characters:

    ```
    size(this) <= 20000
    ```
    """

    draft: bool

    title: str
    """Title must be between 1 and 500 characters:

    ```
    size(this) >= 1 && size(this) <= 500
    ```
    """


class Task(TypedDict, total=False):
    """WorkflowTaskStep represents a task step that executes a command."""

    command: str
    """Command must be between 1 and 20,000 characters:

    ```
    size(this) >= 1 && size(this) <= 20000
    ```
    """


class WorkflowStepParam(TypedDict, total=False):
    """WorkflowStep defines a single step in a workflow action."""

    agent: Agent
    """WorkflowAgentStep represents an agent step that executes with a prompt."""

    pull_request: Annotated[PullRequest, PropertyInfo(alias="pullRequest")]
    """WorkflowPullRequestStep represents a pull request creation step."""

    task: Task
    """WorkflowTaskStep represents a task step that executes a command."""
