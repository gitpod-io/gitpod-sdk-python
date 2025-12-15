# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .runner_kind import RunnerKind
from .runner_spec import RunnerSpec
from .runner_status import RunnerStatus
from .shared.subject import Subject
from .runner_provider import RunnerProvider

__all__ = ["Runner"]


class Runner(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time when the Runner was created."""

    creator: Optional[Subject] = None
    """creator is the identity of the creator of the environment"""

    kind: Optional[RunnerKind] = None
    """The runner's kind"""

    name: Optional[str] = None
    """The runner's name which is shown to users"""

    provider: Optional[RunnerProvider] = None
    """The runner's provider"""

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)

    runner_manager_id: Optional[str] = FieldInfo(alias="runnerManagerId", default=None)
    """
    The runner manager id specifies the runner manager for the managed runner. This
    field is only set for managed runners.
    """

    spec: Optional[RunnerSpec] = None
    """The runner's specification"""

    status: Optional[RunnerStatus] = None
    """The runner's status"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time when the Runner was last udpated."""
