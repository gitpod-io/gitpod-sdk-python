# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .environment_spec import EnvironmentSpec
from .environment_status import EnvironmentStatus
from .environment_metadata import EnvironmentMetadata

__all__ = ["Environment"]


class Environment(BaseModel):
    id: str
    """ID is a unique identifier of this environment.

    No other environment with the same name must be managed by this environment
    manager
    """

    metadata: Optional[EnvironmentMetadata] = None
    """
    EnvironmentMetadata is data associated with an environment that's required for
    other parts of the system to function
    """

    spec: Optional[EnvironmentSpec] = None
    """
    EnvironmentSpec specifies the configuration of an environment for an environment
    start
    """

    status: Optional[EnvironmentStatus] = None
    """EnvironmentStatus describes an environment status"""
