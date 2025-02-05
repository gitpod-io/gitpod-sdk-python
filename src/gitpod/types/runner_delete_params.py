# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerDeleteParams"]


class RunnerDeleteParams(TypedDict, total=False):
    force: bool
    """
    force indicates whether the runner should be deleted forcefully. When force
    deleting a Runner, all Environments on the runner are also force deleted and
    regular Runner lifecycle is not respected. Force deleting can result in data
    loss.
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
