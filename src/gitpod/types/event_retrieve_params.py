# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventRetrieveParams"]


class EventRetrieveParams(TypedDict, total=False):
    audit_log_entry_id: Required[Annotated[str, PropertyInfo(alias="auditLogEntryId")]]
    """audit_log_entry_id is the ID of the audit-log entry to retrieve."""
