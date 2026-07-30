# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerListScmOrganizationsParams", "Pagination"]


class RunnerListScmOrganizationsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    pagination: Pagination
    """Pagination parameters.

    When unset, defaults to the standard PaginationRequest defaults (page_size 25,
    max 100). Tokens are opaque and provider-specific.
    """

    query: str
    """Optional substring filter applied to the organization name.

    - GitLab: forwarded to the upstream `search` parameter (server-side,
      case-insensitive substring on name/path).
    - GitHub and Bitbucket: not implemented as they don't support searching Empty
      value means no filter.
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_host: Annotated[str, PropertyInfo(alias="scmHost")]
    """The SCM host to list organizations from (e.g., "github.com", "gitlab.com")"""


class Pagination(TypedDict, total=False):
    """Pagination parameters.

    When unset, defaults to the standard PaginationRequest defaults
     (page_size 25, max 100). Tokens are opaque and provider-specific.
    """

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
