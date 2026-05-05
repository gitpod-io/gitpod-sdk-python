# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WorkflowTriggerContextParam",
    "Agent",
    "Projects",
    "Repositories",
    "RepositoriesRepoSelector",
    "RepositoriesRepositoryURLs",
]


class Agent(TypedDict, total=False):
    """
    Execute workflow in agent-managed environments.
     Agent receives the specified prompt and manages execution context.
    """

    prompt: str
    """Agent prompt must be between 1 and 20,000 characters:

    ```
    size(this) >= 1 && size(this) <= 20000
    ```
    """


class Projects(TypedDict, total=False):
    """
    Execute workflow in specific project environments.
     Creates environments for each specified project.
    """

    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]


class RepositoriesRepoSelector(TypedDict, total=False):
    """
    RepositorySelector defines how to select repositories for workflow execution.
     Combines a search string with an SCM host to identify repositories.
    """

    repo_search_string: Annotated[str, PropertyInfo(alias="repoSearchString")]
    """
    Search string to match repositories using SCM-specific search patterns. For
    GitHub: supports GitHub search syntax (e.g., "org:gitpod-io language:go",
    "user:octocat stars:>100") For GitLab: supports GitLab search syntax See SCM
    provider documentation for supported search patterns.
    """

    scm_host: Annotated[str, PropertyInfo(alias="scmHost")]
    """
    SCM host where the search should be performed (e.g., "github.com", "gitlab.com")
    """


class RepositoriesRepositoryURLs(TypedDict, total=False):
    """
    RepositoryURLs contains a list of explicit repository URLs.
     Creates one action per repository URL.
    """

    repo_urls: Annotated[SequenceNotStr[str], PropertyInfo(alias="repoUrls")]


class Repositories(TypedDict, total=False):
    """
    Execute workflow in environments created from repository URLs.
     Supports both explicit repository URLs and search patterns.
    """

    environment_class_id: Annotated[str, PropertyInfo(alias="environmentClassId")]

    repo_selector: Annotated[RepositoriesRepoSelector, PropertyInfo(alias="repoSelector")]
    """
    RepositorySelector defines how to select repositories for workflow execution.
    Combines a search string with an SCM host to identify repositories.
    """

    repository_urls: Annotated[RepositoriesRepositoryURLs, PropertyInfo(alias="repositoryUrls")]
    """
    RepositoryURLs contains a list of explicit repository URLs. Creates one action
    per repository URL.
    """


class WorkflowTriggerContextParam(TypedDict, total=False):
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
    - Incident: Typically uses Projects or Repositories context (no inherent repo context)
    """

    agent: Agent
    """
    Execute workflow in agent-managed environments. Agent receives the specified
    prompt and manages execution context.
    """

    from_trigger: Annotated[object, PropertyInfo(alias="fromTrigger")]
    """
    Use context derived from the trigger event. Currently only supported for
    PullRequest triggers - uses PR repository context.
    """

    projects: Projects
    """
    Execute workflow in specific project environments. Creates environments for each
    specified project.
    """

    repositories: Repositories
    """
    Execute workflow in environments created from repository URLs. Supports both
    explicit repository URLs and search patterns.
    """
