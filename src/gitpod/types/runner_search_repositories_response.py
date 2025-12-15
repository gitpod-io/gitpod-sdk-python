# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerSearchRepositoriesResponse", "Pagination", "Repository"]


class Pagination(BaseModel):
    """Pagination information for the response"""

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
    """Last page in the responses"""

    pagination: Optional[Pagination] = None
    """Pagination information for the response"""

    repositories: Optional[List[Repository]] = None
    """List of repositories matching the search criteria"""
