# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnvironmentInitializer", "Spec", "SpecContextURL", "SpecGit"]


class SpecContextURL(BaseModel):
    url: Optional[str] = None
    """url is the URL from which the environment is created"""


class SpecGit(BaseModel):
    checkout_location: Optional[str] = FieldInfo(alias="checkoutLocation", default=None)
    """
    a path relative to the environment root in which the code will be checked out to
    """

    clone_target: Optional[str] = FieldInfo(alias="cloneTarget", default=None)
    """the value for the clone target mode - use depends on the target mode"""

    remote_uri: Optional[str] = FieldInfo(alias="remoteUri", default=None)
    """remote_uri is the Git remote origin"""

    target_mode: Optional[
        Literal[
            "CLONE_TARGET_MODE_UNSPECIFIED",
            "CLONE_TARGET_MODE_REMOTE_HEAD",
            "CLONE_TARGET_MODE_REMOTE_COMMIT",
            "CLONE_TARGET_MODE_REMOTE_BRANCH",
            "CLONE_TARGET_MODE_LOCAL_BRANCH",
        ]
    ] = FieldInfo(alias="targetMode", default=None)
    """CloneTargetMode is the target state in which we want to leave a GitEnvironment"""

    upstream_remote_uri: Optional[str] = FieldInfo(alias="upstreamRemoteUri", default=None)
    """upstream_Remote_uri is the fork upstream of a repository"""


class Spec(BaseModel):
    context_url: Optional[SpecContextURL] = FieldInfo(alias="contextUrl", default=None)

    git: Optional[SpecGit] = None


class EnvironmentInitializer(BaseModel):
    specs: Optional[List[Spec]] = None
