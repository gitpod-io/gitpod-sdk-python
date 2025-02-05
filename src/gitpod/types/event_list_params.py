# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams", "Filter", "Pagination"]


class EventListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""


class Filter(TypedDict, total=False):
    actor_ids: Annotated[List[str], PropertyInfo(alias="actorIds")]

    actor_principals: Annotated[
        List[
            Literal[
                "PRINCIPAL_UNSPECIFIED",
                "PRINCIPAL_ACCOUNT",
                "PRINCIPAL_USER",
                "PRINCIPAL_RUNNER",
                "PRINCIPAL_ENVIRONMENT",
                "PRINCIPAL_SERVICE_ACCOUNT",
            ]
        ],
        PropertyInfo(alias="actorPrincipals"),
    ]

    subject_ids: Annotated[List[str], PropertyInfo(alias="subjectIds")]

    subject_types: Annotated[
        List[
            Literal[
                "RESOURCE_TYPE_UNSPECIFIED",
                "RESOURCE_TYPE_ENVIRONMENT",
                "RESOURCE_TYPE_RUNNER",
                "RESOURCE_TYPE_PROJECT",
                "RESOURCE_TYPE_TASK",
                "RESOURCE_TYPE_TASK_EXECUTION",
                "RESOURCE_TYPE_SERVICE",
                "RESOURCE_TYPE_ORGANIZATION",
                "RESOURCE_TYPE_USER",
                "RESOURCE_TYPE_ENVIRONMENT_CLASS",
                "RESOURCE_TYPE_RUNNER_SCM_INTEGRATION",
                "RESOURCE_TYPE_HOST_AUTHENTICATION_TOKEN",
                "RESOURCE_TYPE_GROUP",
                "RESOURCE_TYPE_PERSONAL_ACCESS_TOKEN",
                "RESOURCE_TYPE_USER_PREFERENCE",
                "RESOURCE_TYPE_SERVICE_ACCOUNT",
                "RESOURCE_TYPE_SECRET",
                "RESOURCE_TYPE_SSO_CONFIG",
            ]
        ],
        PropertyInfo(alias="subjectTypes"),
    ]


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
