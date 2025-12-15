# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCodeContextParam", "ContextURL", "PullRequest", "PullRequestRepository"]


class ContextURL(TypedDict, total=False):
    environment_class_id: Annotated[str, PropertyInfo(alias="environmentClassId")]

    url: str


class PullRequestRepository(TypedDict, total=False):
    """Repository information"""

    clone_url: Annotated[str, PropertyInfo(alias="cloneUrl")]

    host: str

    name: str

    owner: str


class PullRequest(TypedDict, total=False):
    """
    Pull request context - optional metadata about the PR being worked on
     This is populated when the agent execution is triggered by a PR workflow
     or when explicitly provided through the browser extension
    """

    id: str
    """Unique identifier from the source system (e.g., "123" for GitHub PR #123)"""

    author: str
    """Author name as provided by the SCM system"""

    from_branch: Annotated[str, PropertyInfo(alias="fromBranch")]
    """Source branch name (the branch being merged from)"""

    repository: PullRequestRepository
    """Repository information"""

    title: str
    """Pull request title"""

    to_branch: Annotated[str, PropertyInfo(alias="toBranch")]
    """Target branch name (the branch being merged into)"""

    url: str
    """Pull request URL (e.g., "https://github.com/owner/repo/pull/123")"""


class AgentCodeContextParam(TypedDict, total=False):
    context_url: Annotated[ContextURL, PropertyInfo(alias="contextUrl")]

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    pull_request: Annotated[Optional[PullRequest], PropertyInfo(alias="pullRequest")]
    """
    Pull request context - optional metadata about the PR being worked on This is
    populated when the agent execution is triggered by a PR workflow or when
    explicitly provided through the browser extension
    """
