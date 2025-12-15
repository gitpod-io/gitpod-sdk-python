# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .crowd_strike_config import CrowdStrikeConfig

__all__ = ["SecurityAgentPolicy"]


class SecurityAgentPolicy(BaseModel):
    """
    SecurityAgentPolicy contains security agent configuration for an organization.
     When enabled, security agents are automatically deployed to all environments.
    """

    crowdstrike: Optional[CrowdStrikeConfig] = None
    """crowdstrike contains CrowdStrike Falcon configuration"""
