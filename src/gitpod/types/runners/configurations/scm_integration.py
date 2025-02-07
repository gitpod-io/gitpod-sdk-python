# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .scm_integration_oauth_config import ScmIntegrationOAuthConfig

__all__ = ["ScmIntegration"]


class ScmIntegration(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the SCM integration"""

    host: Optional[str] = None

    oauth: Optional[ScmIntegrationOAuthConfig] = None

    pat: Optional[bool] = None

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)
    """
    scm_id references the scm_id in the runner's configuration schema that this
    integration is for
    """
