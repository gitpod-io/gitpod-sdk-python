# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .runner import Runner
from .._models import BaseModel

__all__ = ["RunnerRetrieveResponse"]


class RunnerRetrieveResponse(BaseModel):
    runner: Runner
