# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerListScmOrganizationsParams"]


class RunnerListScmOrganizationsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_host: Annotated[str, PropertyInfo(alias="scmHost")]
    """The SCM host to list organizations from (e.g., "github.com", "gitlab.com")"""
