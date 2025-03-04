# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .runner_phase import RunnerPhase
from .runner_capability import RunnerCapability
from .shared.field_value import FieldValue

__all__ = ["RunnerStatus"]


class RunnerStatus(BaseModel):
    additional_info: Optional[List[FieldValue]] = FieldInfo(alias="additionalInfo", default=None)
    """additional_info contains additional information about the runner, e.g.

    a CloudFormation stack URL.
    """

    capabilities: Optional[List[RunnerCapability]] = None
    """capabilities is a list of capabilities the runner supports."""

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)

    message: Optional[str] = None
    """
    The runner's reported message which is shown to users. This message adds more
    context to the runner's phase.
    """

    phase: Optional[RunnerPhase] = None
    """The runner's reported phase"""

    region: Optional[str] = None
    """region is the region the runner is running in, if applicable."""

    system_details: Optional[str] = FieldInfo(alias="systemDetails", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time when the status was last udpated."""

    version: Optional[str] = None
