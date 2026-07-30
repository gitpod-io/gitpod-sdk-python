# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pr_time_bucket import PrTimeBucket

__all__ = ["UsageGetPrTimeSeriesResponse"]


class UsageGetPrTimeSeriesResponse(BaseModel):
    time_series: Optional[List[PrTimeBucket]] = FieldInfo(alias="timeSeries", default=None)
    """Time series of PR speed metrics, bucketed by the requested resolution."""
