# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .runner_phase import RunnerPhase
from .runner_configuration_param import RunnerConfigurationParam

__all__ = ["RunnerSpecParam"]


class RunnerSpecParam(TypedDict, total=False):
    configuration: RunnerConfigurationParam
    """The runner's configuration"""

    desired_phase: Annotated[RunnerPhase, PropertyInfo(alias="desiredPhase")]
    """RunnerPhase represents the phase a runner is in"""
