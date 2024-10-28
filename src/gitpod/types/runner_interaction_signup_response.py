# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerInteractionSignupResponse"]


class RunnerInteractionSignupResponse(BaseModel):
    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)
    """The runner's identity"""
