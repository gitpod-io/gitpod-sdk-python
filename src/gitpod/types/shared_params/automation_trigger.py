# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AutomationTrigger"]


class AutomationTrigger(TypedDict, total=False):
    """
    An AutomationTrigger represents a trigger for an automation action.
     The `post_environment_start` field indicates that the automation should be triggered after the environment has started.
     The `post_devcontainer_start` field indicates that the automation should be triggered after the dev container has started.
    """

    manual: bool

    post_devcontainer_start: Annotated[bool, PropertyInfo(alias="postDevcontainerStart")]

    post_environment_start: Annotated[bool, PropertyInfo(alias="postEnvironmentStart")]
