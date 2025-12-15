# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerParseContextURLResponse", "Git", "Issue", "Pr", "PullRequest", "PullRequestRepository"]


class Git(BaseModel):
    branch: Optional[str] = None

    clone_url: Optional[str] = FieldInfo(alias="cloneUrl", default=None)

    commit: Optional[str] = None

    host: Optional[str] = None

    owner: Optional[str] = None

    repo: Optional[str] = None

    tag: Optional[str] = None

    upstream_remote_url: Optional[str] = FieldInfo(alias="upstreamRemoteUrl", default=None)


class Issue(BaseModel):
    id: Optional[str] = None
    """id is the source system's ID of this issue, e.g. BNFRD-6100"""

    title: Optional[str] = None


class Pr(BaseModel):
    """Deprecated: Use top-level PullRequest message instead"""

    id: Optional[str] = None

    from_branch: Optional[str] = FieldInfo(alias="fromBranch", default=None)

    title: Optional[str] = None

    to_branch: Optional[str] = FieldInfo(alias="toBranch", default=None)


class PullRequestRepository(BaseModel):
    """Repository information"""

    clone_url: Optional[str] = FieldInfo(alias="cloneUrl", default=None)

    host: Optional[str] = None

    name: Optional[str] = None

    owner: Optional[str] = None


class PullRequest(BaseModel):
    """
    PullRequest represents pull request metadata from source control systems.
     This message is used across workflow triggers, executions, and agent contexts
     to maintain consistent PR information throughout the system.
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


class RunnerParseContextURLResponse(BaseModel):
    git: Optional[Git] = None

    issue: Optional[Issue] = None

    original_context_url: Optional[str] = FieldInfo(alias="originalContextUrl", default=None)

    pr: Optional[Pr] = None
    """Deprecated: Use top-level PullRequest message instead"""

    project_ids: Optional[List[str]] = FieldInfo(alias="projectIds", default=None)
    """project_ids is a list of projects to which the context URL belongs to."""

    pull_request: Optional[PullRequest] = FieldInfo(alias="pullRequest", default=None)
    """
    PullRequest represents pull request metadata from source control systems. This
    message is used across workflow triggers, executions, and agent contexts to
    maintain consistent PR information throughout the system.
    """

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)
    """
    scm_id is the unique identifier of the SCM provider (e.g., "github", "gitlab",
    "bitbucket")
    """
