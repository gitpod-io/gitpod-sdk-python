# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AutomationTrigger"]


class AutomationTrigger(TypedDict, total=False):
    """
    An AutomationTrigger represents a trigger for an automation action.
     The `manual` field shows a start button in the UI for manually triggering the automation.
     The `post_machine_start` field indicates that the automation should be triggered after the machine has started, before the devcontainer is ready.
     This is used for machine-level services like security agents that need to start early.
     The `post_environment_start` field indicates that the automation should be triggered after the environment has started (devcontainer ready).
     The `post_devcontainer_start` field indicates that the automation should be triggered after the dev container has started.
     The `prebuild` field starts the automation during a prebuild of an environment. This phase does not have user secrets available.
     The `before_snapshot` field triggers the automation after all prebuild tasks complete but before the snapshot is taken.
     This is used for tasks that need to run last during prebuilds, such as IDE warmup.
     Note: The prebuild and before_snapshot triggers can only be used with tasks, not services.
    """

    before_snapshot: Annotated[bool, PropertyInfo(alias="beforeSnapshot")]

    manual: bool

    post_devcontainer_start: Annotated[bool, PropertyInfo(alias="postDevcontainerStart")]

    post_environment_start: Annotated[bool, PropertyInfo(alias="postEnvironmentStart")]

    post_machine_start: Annotated[bool, PropertyInfo(alias="postMachineStart")]

    prebuild: bool
