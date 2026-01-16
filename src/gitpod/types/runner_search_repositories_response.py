# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerSearchRepositoriesResponse", "Pagination", "Repository"]


class Pagination(BaseModel):
    """
    Pagination information for the response.
     Token format: "NEXT_PAGE/TOTAL_PAGES/TOTAL_COUNT" (e.g., "2/40/1000").
     Use -1 for unknown values (e.g., "2/-1/-1" when totals unavailable).
     Empty token means no more pages.
    """

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retrieving the next set of results.

    Empty if there are no more results
    """


class Repository(BaseModel):
    name: Optional[str] = None
    """Repository name (e.g., "my-project")"""

    url: Optional[str] = None
    """Repository URL (e.g., "https://github.com/owner/my-project")"""


class RunnerSearchRepositoriesResponse(BaseModel):
    last_page: Optional[int] = FieldInfo(alias="lastPage", default=None)
    """Deprecated: Use pagination token instead.

    Total pages can be extracted from token.
    """

    pagination: Optional[Pagination] = None
    """
    Pagination information for the response. Token format:
    "NEXT_PAGE/TOTAL_PAGES/TOTAL_COUNT" (e.g., "2/40/1000"). Use -1 for unknown
    values (e.g., "2/-1/-1" when totals unavailable). Empty token means no more
    pages.
    """

    repositories: Optional[List[Repository]] = None
    """List of repositories matching the search criteria"""
