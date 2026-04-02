# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowStep", "Agent", "PullRequest", "Task"]


class Agent(BaseModel):
    """WorkflowAgentStep represents an agent step that executes with a prompt."""

    prompt: Optional[str] = None
    """Prompt must be between 1 and 20,000 characters:

    ```
    size(this) >= 1 && size(this) <= 20000
    ```
    """


class PullRequest(BaseModel):
    """WorkflowPullRequestStep represents a pull request creation step."""

    branch: Optional[str] = None
    """Branch name must be between 1 and 255 characters:

    ```
    size(this) >= 1 && size(this) <= 255
    ```
    """

    description: Optional[str] = None
    """Description must be at most 20,000 characters:

    ```
    size(this) <= 20000
    ```
    """

    draft: Optional[bool] = None

    title: Optional[str] = None
    """Title must be between 1 and 500 characters:

    ```
    size(this) >= 1 && size(this) <= 500
    ```
    """


class Task(BaseModel):
    """WorkflowTaskStep represents a task step that executes a command."""

    command: Optional[str] = None
    """Command must be between 1 and 20,000 characters:

    ```
    size(this) >= 1 && size(this) <= 20000
    ```
    """


class WorkflowStep(BaseModel):
    """WorkflowStep defines a single step in a workflow action."""

    agent: Optional[Agent] = None
    """WorkflowAgentStep represents an agent step that executes with a prompt."""

    pull_request: Optional[PullRequest] = FieldInfo(alias="pullRequest", default=None)
    """WorkflowPullRequestStep represents a pull request creation step."""

    task: Optional[Task] = None
    """WorkflowTaskStep represents a task step that executes a command."""
