# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentInitializerParam", "Spec", "SpecContextURL", "SpecGit"]


class SpecContextURL(TypedDict, total=False):
    url: str
    """url is the URL from which the environment is created"""


class SpecGit(TypedDict, total=False):
    checkout_location: Annotated[str, PropertyInfo(alias="checkoutLocation")]
    """
    a path relative to the environment root in which the code will be checked out to
    """

    clone_target: Annotated[str, PropertyInfo(alias="cloneTarget")]
    """the value for the clone target mode - use depends on the target mode"""

    remote_uri: Annotated[str, PropertyInfo(alias="remoteUri")]
    """remote_uri is the Git remote origin"""

    target_mode: Annotated[
        Literal[
            "CLONE_TARGET_MODE_UNSPECIFIED",
            "CLONE_TARGET_MODE_REMOTE_HEAD",
            "CLONE_TARGET_MODE_REMOTE_COMMIT",
            "CLONE_TARGET_MODE_REMOTE_BRANCH",
            "CLONE_TARGET_MODE_LOCAL_BRANCH",
        ],
        PropertyInfo(alias="targetMode"),
    ]
    """CloneTargetMode is the target state in which we want to leave a GitEnvironment"""

    upstream_remote_uri: Annotated[str, PropertyInfo(alias="upstreamRemoteUri")]
    """upstream_Remote_uri is the fork upstream of a repository"""


class Spec(TypedDict, total=False):
    context_url: Annotated[SpecContextURL, PropertyInfo(alias="contextUrl")]

    git: SpecGit


class EnvironmentInitializerParam(TypedDict, total=False):
    specs: Iterable[Spec]
