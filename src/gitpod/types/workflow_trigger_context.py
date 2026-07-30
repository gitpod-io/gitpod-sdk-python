# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WorkflowTriggerContext",
    "Agent",
    "Projects",
    "Repositories",
    "RepositoriesRepoSelector",
    "RepositoriesRepositoryURLs",
]


class Agent(BaseModel):
    """
    Execute workflow in agent-managed environments.
     Agent receives the specified prompt and manages execution context.
    """

    prompt: Optional[str] = None
    """Agent prompt must be between 1 and 20,000 characters:

    ```
    size(this) >= 1 && size(this) <= 20000
    ```
    """


class Projects(BaseModel):
    """
    Execute workflow in specific project environments.
     Creates environments for each specified project.
    """

    project_ids: Optional[List[str]] = FieldInfo(alias="projectIds", default=None)


class RepositoriesRepoSelector(BaseModel):
    """
    RepositorySelector defines how to select repositories for workflow execution.
     Combines a search string with an SCM host to identify repositories.
    """

    repo_search_string: Optional[str] = FieldInfo(alias="repoSearchString", default=None)
    """
    Search string to match repositories using SCM-specific search patterns. For
    GitHub: supports GitHub search syntax (e.g., "org:gitpod-io language:go",
    "user:octocat stars:>100") For GitLab: supports GitLab search syntax See SCM
    provider documentation for supported search patterns.
    """

    scm_host: Optional[str] = FieldInfo(alias="scmHost", default=None)
    """
    SCM host where the search should be performed (e.g., "github.com", "gitlab.com")
    """


class RepositoriesRepositoryURLs(BaseModel):
    """
    RepositoryURLs contains a list of explicit repository URLs.
     Creates one action per repository URL.
    """

    repo_urls: Optional[List[str]] = FieldInfo(alias="repoUrls", default=None)


class Repositories(BaseModel):
    """
    Execute workflow in environments created from repository URLs.
     Supports both explicit repository URLs and search patterns.
    """

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)

    repo_selector: Optional[RepositoriesRepoSelector] = FieldInfo(alias="repoSelector", default=None)
    """
    RepositorySelector defines how to select repositories for workflow execution.
    Combines a search string with an SCM host to identify repositories.
    """

    repository_urls: Optional[RepositoriesRepositoryURLs] = FieldInfo(alias="repositoryUrls", default=None)
    """
    RepositoryURLs contains a list of explicit repository URLs. Creates one action
    per repository URL.
    """


class WorkflowTriggerContext(BaseModel):
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

    agent: Optional[Agent] = None
    """
    Execute workflow in agent-managed environments. Agent receives the specified
    prompt and manages execution context.
    """

    from_trigger: Optional[object] = FieldInfo(alias="fromTrigger", default=None)
    """
    Use context derived from the trigger event. Currently only supported for
    PullRequest triggers - uses PR repository context.
    """

    projects: Optional[Projects] = None
    """
    Execute workflow in specific project environments. Creates environments for each
    specified project.
    """

    repositories: Optional[Repositories] = None
    """
    Execute workflow in environments created from repository URLs. Supports both
    explicit repository URLs and search patterns.
    """
