# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .runner_kind import RunnerKind
from .runner_provider import RunnerProvider
from .runner_spec_param import RunnerSpecParam

__all__ = ["RunnerCreateParams"]


class RunnerCreateParams(TypedDict, total=False):
    kind: RunnerKind
    """The runner's kind This field is optional and here for backwards-compatibility.

    Use the provider field instead. If provider is set, the runner's kind will be
    deduced from the provider. Only one of kind and provider must be set.
    """

    name: str
    """The runner name for humans"""

    provider: RunnerProvider
    """
    The specific implementation type of the runner This field is optional for
    backwards compatibility but will be required in the future. When specified, kind
    must not be specified (will be deduced from provider)
    """

    runner_manager_id: Annotated[str, PropertyInfo(alias="runnerManagerId")]
    """
    The runner manager id specifies the runner manager for the managed runner. This
    field is mandatory for managed runners, otheriwse should not be set.
    """

    spec: RunnerSpecParam
