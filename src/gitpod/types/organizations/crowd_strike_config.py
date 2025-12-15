# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrowdStrikeConfig"]


class CrowdStrikeConfig(BaseModel):
    """CrowdStrikeConfig configures CrowdStrike Falcon sensor deployment"""

    additional_options: Optional[Dict[str, str]] = FieldInfo(alias="additionalOptions", default=None)
    """
    additional*options contains additional FALCONCTL_OPT*\\** options as key-value
    pairs. Keys should NOT include the FALCONCTL*OPT* prefix.
    """

    cid_secret_id: Optional[str] = FieldInfo(alias="cidSecretId", default=None)
    """
    cid_secret_id references an organization secret containing the Customer ID
    (CID).
    """

    enabled: Optional[bool] = None
    """enabled controls whether CrowdStrike Falcon is deployed to environments"""

    image: Optional[str] = None
    """image is the CrowdStrike Falcon sensor container image reference"""

    tags: Optional[str] = None
    """tags are optional tags to apply to the Falcon sensor (comma-separated)"""
