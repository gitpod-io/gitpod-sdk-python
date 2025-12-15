# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerCreateLogsTokenParams"]


class RunnerCreateLogsTokenParams(TypedDict, total=False):
    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """runner_id specifies the runner for which the logs token should be created.

    +required
    """
