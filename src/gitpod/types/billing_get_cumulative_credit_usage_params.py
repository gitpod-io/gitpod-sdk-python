# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BillingGetCumulativeCreditUsageParams"]


class BillingGetCumulativeCreditUsageParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to get cumulative usage for."""

    as_of: Annotated[Union[str, datetime, None], PropertyInfo(alias="asOf", format="iso8601")]
    """
    as_of is the point in time to compute cumulative usage up to. Defaults to now if
    not set.
    """
