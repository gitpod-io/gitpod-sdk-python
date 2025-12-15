# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentCodeContext", "ContextURL", "PullRequest", "PullRequestRepository"]


class ContextURL(BaseModel):
    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)

    url: Optional[str] = None


class PullRequestRepository(BaseModel):
    """Repository information"""

    clone_url: Optional[str] = FieldInfo(alias="cloneUrl", default=None)

    host: Optional[str] = None

    name: Optional[str] = None

    owner: Optional[str] = None


class PullRequest(BaseModel):
    """
    Pull request context - optional metadata about the PR being worked on
     This is populated when the agent execution is triggered by a PR workflow
     or when explicitly provided through the browser extension
    """

    id: Optional[str] = None
    """Unique identifier from the source system (e.g., "123" for GitHub PR #123)"""

    author: Optional[str] = None
    """Author name as provided by the SCM system"""

    from_branch: Optional[str] = FieldInfo(alias="fromBranch", default=None)
    """Source branch name (the branch being merged from)"""

    repository: Optional[PullRequestRepository] = None
    """Repository information"""

    title: Optional[str] = None
    """Pull request title"""

    to_branch: Optional[str] = FieldInfo(alias="toBranch", default=None)
    """Target branch name (the branch being merged into)"""

    url: Optional[str] = None
    """Pull request URL (e.g., "https://github.com/owner/repo/pull/123")"""


class AgentCodeContext(BaseModel):
    context_url: Optional[ContextURL] = FieldInfo(alias="contextUrl", default=None)

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    pull_request: Optional[PullRequest] = FieldInfo(alias="pullRequest", default=None)
    """
    Pull request context - optional metadata about the PR being worked on This is
    populated when the agent execution is triggered by a PR workflow or when
    explicitly provided through the browser extension
    """
