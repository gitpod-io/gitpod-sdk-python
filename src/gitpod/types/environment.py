# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .environment_spec import EnvironmentSpec
from .environment_status import EnvironmentStatus
from .environment_metadata import EnvironmentMetadata

__all__ = ["Environment"]


class Environment(BaseModel):
    """+resource get environment"""

    id: str
    """ID is a unique identifier of this environment.

    No other environment with the same name must be managed by this environment
    manager
    """

    metadata: Optional[EnvironmentMetadata] = None
    """
    Metadata is data associated with this environment that's required for other
    parts of Gitpod to function
    """

    spec: Optional[EnvironmentSpec] = None
    """
    Spec is the configuration of the environment that's required for the runner to
    start the environment
    """

    status: Optional[EnvironmentStatus] = None
    """Status is the current status of the environment"""
