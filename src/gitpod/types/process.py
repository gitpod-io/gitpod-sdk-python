# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Process"]


class Process(BaseModel):
    """Process describes process metadata for a security event.

    PID fields use int32 to match the kernel's pid_t (signed int).
    Linux PID max is 4,194,304 (2^22), well within int32 range.
    Postgres has no unsigned integer type: Ent maps uint32 to bigint
    (8 bytes) while int32 maps to integer (4 bytes). Using int32
    aligns proto, Go, and Postgres types without wasting storage.
    """

    name: Optional[str] = None
    """name is the process name (comm). 2x kernel TASK_COMM_LEN=16"""

    pgid: Optional[int] = None
    """pgid is the process group ID."""

    pid: Optional[int] = None
    """pid is the userspace process ID (kernel thread group ID, tgid)."""

    ppid: Optional[int] = None
    """ppid is the parent process ID."""

    sid: Optional[int] = None
    """sid is the session ID."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """started_at is when the process started."""

    tid: Optional[int] = None
    """tid is the userspace thread ID (kernel pid)."""
