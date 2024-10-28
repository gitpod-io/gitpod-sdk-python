# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerInteractionListRunnerScmIntegrationsResponse", "Pagination"]


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


class RunnerInteractionListRunnerScmIntegrationsResponse(BaseModel):
    pagination: Optional[Pagination] = None
    """pagination contains the pagination options for listing SCM integrations"""

    scm_integrations: Optional[List[Union[object, object]]] = FieldInfo(alias="scmIntegrations", default=None)
    """The SCM integrations configured for the runner"""
