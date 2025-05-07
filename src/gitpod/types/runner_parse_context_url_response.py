# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerParseContextURLResponse", "Git"]


class Git(BaseModel):
    branch: Optional[str] = None

    clone_url: Optional[str] = FieldInfo(alias="cloneUrl", default=None)

    commit: Optional[str] = None

    host: Optional[str] = None

    owner: Optional[str] = None

    repo: Optional[str] = None

    upstream_remote_url: Optional[str] = FieldInfo(alias="upstreamRemoteUrl", default=None)


class RunnerParseContextURLResponse(BaseModel):
    git: Optional[Git] = None

    original_context_url: Optional[str] = FieldInfo(alias="originalContextUrl", default=None)

    project_ids: Optional[List[str]] = FieldInfo(alias="projectIds", default=None)
    """project_ids is a list of projects to which the context URL belongs to."""
