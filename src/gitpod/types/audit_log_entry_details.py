# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .process import Process
from .._models import BaseModel
from .shared.kernel_controls_action import KernelControlsAction

__all__ = ["AuditLogEntryDetails", "VetoExec"]


class VetoExec(BaseModel):
    """veto_exec contains Veto Exec event details without process.cmdline."""

    process: Process
    """process contains metadata about the process that triggered the event."""

    timestamp: datetime
    """timestamp is when the event occurred in the environment."""

    action: Optional[KernelControlsAction] = None
    """action is the enforcement action taken (block or audit)."""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)
    """environment_id is the environment where the event occurred."""

    executable: Optional[str] = None
    """
    executable is the digest of the binary content (e.g., "sha256:a1b2c3d4..."). 256
    allows for longer hash algorithms or prefixed identifiers. May be empty when the
    event source cannot compute the hash.
    """

    filename: Optional[str] = None
    """
    filename is the kernel-resolved path of the binary. Kernel PATH_MAX = 4096
    (include/uapi/linux/limits.h). May be empty if the event source could not
    resolve it.
    """


class AuditLogEntryDetails(BaseModel):
    """
    AuditLogEntryDetails contains the typed evidence stored with an audit-log entry.
    """

    veto_exec: VetoExec = FieldInfo(alias="vetoExec")
    """veto_exec contains Veto Exec event details without process.cmdline."""
