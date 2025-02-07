# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .runner_phase import RunnerPhase
from .runner_configuration import RunnerConfiguration

__all__ = ["RunnerSpec"]


class RunnerSpec(BaseModel):
    configuration: Optional[RunnerConfiguration] = None
    """The runner's configuration"""

    desired_phase: Optional[RunnerPhase] = FieldInfo(alias="desiredPhase", default=None)
    """RunnerPhase represents the phase a runner is in"""
