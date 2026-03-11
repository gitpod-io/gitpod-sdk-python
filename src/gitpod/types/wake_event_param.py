# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WakeEventParam", "Timer"]


class Timer(TypedDict, total=False):
    fired_at: Annotated[Union[str, datetime], PropertyInfo(alias="firedAt", format="iso8601")]
    """The actual time the timer was evaluated as expired."""


class WakeEventParam(TypedDict, total=False):
    """
    WakeEvent is sent by the backend to wake an agent when a registered interest fires.
     Delivered via SendToAgentExecution as a new oneof variant.
    """

    timer: Required[Timer]

    interest_id: Annotated[str, PropertyInfo(alias="interestId")]
    """The interest ID that fired (from WaitingInfo.Interest.id)."""
