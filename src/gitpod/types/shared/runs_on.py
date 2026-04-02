# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RunsOn", "Docker"]


class Docker(BaseModel):
    environment: Optional[List[str]] = None

    image: Optional[str] = None


class RunsOn(BaseModel):
    docker: Optional[Docker] = None

    machine: Optional[object] = None
    """Machine runs the service/task directly on the VM/machine level."""

    terminal: Optional[object] = None
    """
    Terminal runs the service inside a managed PTY terminal in the devcontainer.
    Users can attach to the terminal interactively via the terminal API.
    """
