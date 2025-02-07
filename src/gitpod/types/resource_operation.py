# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ResourceOperation"]

ResourceOperation: TypeAlias = Literal[
    "RESOURCE_OPERATION_UNSPECIFIED",
    "RESOURCE_OPERATION_CREATE",
    "RESOURCE_OPERATION_UPDATE",
    "RESOURCE_OPERATION_DELETE",
    "RESOURCE_OPERATION_UPDATE_STATUS",
]
