# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.subject import Subject

__all__ = ["CreditUsageReportFilterParam"]


class CreditUsageReportFilterParam(TypedDict, total=False):
    """
    CreditUsageReportFilter narrows the data returned by GetCreditUsageReport.
     Wrapping filters in a message (rather than adding bare fields) lets future
     filters (team, environment, resource kind) be added without further breaking
     changes.
    """

    subject: Optional[Subject]
    """Restrict the per-user breakdown to a single subject.

    The subject must be PRINCIPAL_USER or PRINCIPAL_SERVICE_ACCOUNT and belong to
    the request's organization. When unset, the report returns the default top-N
    users + "Others" breakdown.

    When this field is set:

    - daily_usage[*].user_usage contains rows only for the requested subject; no
      "Others" aggregation bucket is produced.
    - daily_usage[*].org_usage, team_usage, environment_usage, and
      conversation_usage are omitted (empty). Callers that need those sections
      should issue an unfiltered call.
    - period_start and updated_at remain populated.
    """
