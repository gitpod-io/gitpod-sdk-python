# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AutomationTrigger"]


class AutomationTrigger(BaseModel):
    """
    An AutomationTrigger represents a trigger for an automation action.
     The `post_environment_start` field indicates that the automation should be triggered after the environment has started.
     The `post_devcontainer_start` field indicates that the automation should be triggered after the dev container has started.
    """

    manual: Optional[bool] = None

    post_devcontainer_start: Optional[bool] = FieldInfo(alias="postDevcontainerStart", default=None)

    post_environment_start: Optional[bool] = FieldInfo(alias="postEnvironmentStart", default=None)
