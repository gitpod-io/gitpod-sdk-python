# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectCreationDefaults"]


class ProjectCreationDefaults(BaseModel):
    """
    ProjectCreationDefaults contains default settings applied to newly created projects.
    """

    insights_enabled: Optional[bool] = FieldInfo(alias="insightsEnabled", default=None)
    """
    insights_enabled controls whether Insights (co-author attribution) is
    automatically enabled on newly created projects.
    """
