# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..types import service_update_params
from .._utils import PropertyInfo

__all__ = ["ServiceUpdateParams"]


class ServiceUpdateParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    id: str

    metadata: service_update_params.Metadata

    spec: Union[object, object]
    """Changing the spec of a service is a complex operation.

    The spec of a service can only be updated if the service is in a stopped state.
    If the service is running, it must be stopped first.
    """

    status: service_update_params.Status
    """Service status updates are only expected from the executing environment.

    As a client of this API you are not expected to provide this field. Updating
    this field requires the `environmentservice:update_status` permission.
    """

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
