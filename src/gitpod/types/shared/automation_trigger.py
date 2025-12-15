# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AutomationTrigger"]


class AutomationTrigger(BaseModel):
    """
    An AutomationTrigger represents a trigger for an automation action.
     The `manual` field shows a start button in the UI for manually triggering the automation.
     The `post_machine_start` field indicates that the automation should be triggered after the machine has started, before the devcontainer is ready.
     This is used for machine-level services like security agents that need to start early.
     The `post_environment_start` field indicates that the automation should be triggered after the environment has started (devcontainer ready).
     The `post_devcontainer_start` field indicates that the automation should be triggered after the dev container has started.
     The `prebuild` field starts the automation during a prebuild of an environment. This phase does not have user secrets available.
     Note: The prebuild trigger can only be used with tasks, not services.
    """

    manual: Optional[bool] = None

    post_devcontainer_start: Optional[bool] = FieldInfo(alias="postDevcontainerStart", default=None)

    post_environment_start: Optional[bool] = FieldInfo(alias="postEnvironmentStart", default=None)

    post_machine_start: Optional[bool] = FieldInfo(alias="postMachineStart", default=None)

    prebuild: Optional[bool] = None
