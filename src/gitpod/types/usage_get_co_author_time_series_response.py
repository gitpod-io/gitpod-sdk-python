# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .co_author_time_bucket import CoAuthorTimeBucket

__all__ = ["UsageGetCoAuthorTimeSeriesResponse"]


class UsageGetCoAuthorTimeSeriesResponse(BaseModel):
    time_series: Optional[List[CoAuthorTimeBucket]] = FieldInfo(alias="timeSeries", default=None)
    """Time series of contribution stats, bucketed by the requested resolution."""
