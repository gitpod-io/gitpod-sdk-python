# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EditorListResponse", "Editor", "Pagination"]


class Editor(BaseModel):
    id: Optional[str] = None

    alias: Optional[str] = None

    icon_url: Optional[str] = FieldInfo(alias="iconUrl", default=None)

    installation_instructions: Optional[str] = FieldInfo(alias="installationInstructions", default=None)

    name: Optional[str] = None

    short_description: Optional[str] = FieldInfo(alias="shortDescription", default=None)

    url_template: Optional[str] = FieldInfo(alias="urlTemplate", default=None)


class Pagination(BaseModel):
    token: Optional[str] = None
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Optional[int] = FieldInfo(alias="pageSize", default=None)
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """


class EditorListResponse(BaseModel):
    editors: Optional[List[Editor]] = None
    """editors contains the list of editors"""

    pagination: Optional[Pagination] = None
    """pagination contains the pagination options for listing environments"""
