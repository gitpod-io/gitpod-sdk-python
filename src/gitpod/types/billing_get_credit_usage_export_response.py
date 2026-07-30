# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BillingGetCreditUsageExportResponse"]


class BillingGetCreditUsageExportResponse(BaseModel):
    download_url: Optional[str] = FieldInfo(alias="downloadUrl", default=None)
    """Signed download URL for the CSV export.

    Valid for five minutes, and only for the principal that requested it.
    """
