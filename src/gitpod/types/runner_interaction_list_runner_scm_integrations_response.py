# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerInteractionListRunnerScmIntegrationsResponse", "Pagination", "ScmIntegration"]


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


class ScmIntegration:
    pass


class RunnerInteractionListRunnerScmIntegrationsResponse(BaseModel):
    pagination: Optional[Pagination] = None
    """pagination contains the pagination options for listing SCM integrations"""

    scm_integrations: Optional[List[ScmIntegration]] = FieldInfo(alias="scmIntegrations", default=None)
    """The SCM integrations configured for the runner"""
