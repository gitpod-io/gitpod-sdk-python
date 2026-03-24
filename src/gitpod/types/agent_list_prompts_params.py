# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentListPromptsParams", "Filter", "Pagination"]


class AgentListPromptsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination


class Filter(TypedDict, total=False):
    command: str

    command_prefix: Annotated[str, PropertyInfo(alias="commandPrefix")]

    exclude_prompt_content: Annotated[bool, PropertyInfo(alias="excludePromptContent")]
    """
    exclude_prompt_content omits the large spec.prompt text from the response. Other
    spec fields (is_template, is_command, command, is_skill) are still returned. Use
    GetPrompt to retrieve the full prompt content when needed.
    """

    is_command: Annotated[bool, PropertyInfo(alias="isCommand")]

    is_skill: Annotated[bool, PropertyInfo(alias="isSkill")]

    is_template: Annotated[bool, PropertyInfo(alias="isTemplate")]

    search: str
    """
    search performs case-insensitive search across prompt name, description, and
    command.
    """


class Pagination(TypedDict, total=False):
    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
