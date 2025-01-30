# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ProjectUpdateParams",
    "AutomationsFilePathIsThePathToTheAutomationsFileRelativeToTheRepoRoot",
    "DevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot",
    "Variant2",
    "Variant2EnvironmentClass",
    "Variant2EnvironmentClassUseAFixedEnvironmentClassOnAGivenRunnerThisCannotBeALocalRunnerSEnvironmentClass",
    "Variant2EnvironmentClassUseALocalRunnerForTheUser",
    "InitializerIsTheContentInitializer",
    "InitializerIsTheContentInitializerInitializer",
    "InitializerIsTheContentInitializerInitializerSpec",
    "InitializerIsTheContentInitializerInitializerSpecContextURL",
    "InitializerIsTheContentInitializerInitializerSpecContextURLContextURL",
    "InitializerIsTheContentInitializerInitializerSpecGit",
    "InitializerIsTheContentInitializerInitializerSpecGitGit",
    "Variant4",
]


class AutomationsFilePathIsThePathToTheAutomationsFileRelativeToTheRepoRoot(TypedDict, total=False):
    automations_file_path: Required[Annotated[str, PropertyInfo(alias="automationsFilePath")]]
    """
    automations_file_path is the path to the automations file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class DevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot(TypedDict, total=False):
    devcontainer_file_path: Required[Annotated[str, PropertyInfo(alias="devcontainerFilePath")]]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant2(TypedDict, total=False):
    environment_class: Required[Annotated[Variant2EnvironmentClass, PropertyInfo(alias="environmentClass")]]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant2EnvironmentClassUseAFixedEnvironmentClassOnAGivenRunnerThisCannotBeALocalRunnerSEnvironmentClass(
    TypedDict, total=False
):
    environment_class_id: Required[Annotated[str, PropertyInfo(alias="environmentClassId")]]
    """Use a fixed environment class on a given Runner.

    This cannot be a local runner's environment class.
    """


class Variant2EnvironmentClassUseALocalRunnerForTheUser(TypedDict, total=False):
    local_runner: Required[Annotated[bool, PropertyInfo(alias="localRunner")]]
    """Use a local runner for the user"""


Variant2EnvironmentClass: TypeAlias = Union[
    Variant2EnvironmentClassUseAFixedEnvironmentClassOnAGivenRunnerThisCannotBeALocalRunnerSEnvironmentClass,
    Variant2EnvironmentClassUseALocalRunnerForTheUser,
]


class InitializerIsTheContentInitializer(TypedDict, total=False):
    initializer: Required[InitializerIsTheContentInitializerInitializer]
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class InitializerIsTheContentInitializerInitializerSpecContextURLContextURL(TypedDict, total=False):
    url: str
    """url is the URL from which the environment is created"""


class InitializerIsTheContentInitializerInitializerSpecContextURL(TypedDict, total=False):
    context_url: Required[
        Annotated[
            InitializerIsTheContentInitializerInitializerSpecContextURLContextURL, PropertyInfo(alias="contextUrl")
        ]
    ]


class InitializerIsTheContentInitializerInitializerSpecGitGit(TypedDict, total=False):
    checkout_location: Annotated[str, PropertyInfo(alias="checkoutLocation")]
    """a path relative to the environment root in which the code will be checked out

    to
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


class InitializerIsTheContentInitializerInitializerSpecGit(TypedDict, total=False):
    git: Required[InitializerIsTheContentInitializerInitializerSpecGitGit]


InitializerIsTheContentInitializerInitializerSpec: TypeAlias = Union[
    InitializerIsTheContentInitializerInitializerSpecContextURL, InitializerIsTheContentInitializerInitializerSpecGit
]


class InitializerIsTheContentInitializerInitializer(TypedDict, total=False):
    specs: Iterable[InitializerIsTheContentInitializerInitializerSpec]


class Variant4(TypedDict, total=False):
    name: Required[str]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


ProjectUpdateParams: TypeAlias = Union[
    AutomationsFilePathIsThePathToTheAutomationsFileRelativeToTheRepoRoot,
    DevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot,
    Variant2,
    InitializerIsTheContentInitializer,
    Variant4,
]
