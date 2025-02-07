# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .runner_kind import RunnerKind
from .runner_provider import RunnerProvider
from .runner_spec_param import RunnerSpecParam

__all__ = ["RunnerCreateParams"]


class RunnerCreateParams(TypedDict, total=False):
    kind: RunnerKind
    """RunnerKind represents the kind of a runner"""

    name: str
    """The runner name for humans"""

    provider: RunnerProvider
    """
    RunnerProvider identifies the specific implementation type of a runner. Each
    provider maps to a specific kind of runner (local or remote), as specified below
    for each provider.
    """

    spec: RunnerSpecParam
