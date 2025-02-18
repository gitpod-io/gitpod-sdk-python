# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .environment import Environment

__all__ = ["EnvironmentCreateFromProjectResponse"]


class EnvironmentCreateFromProjectResponse(BaseModel):
    environment: Environment
    """+resource get environment"""
