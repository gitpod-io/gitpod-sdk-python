# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EnvironmentUpdateParams",
    "Variant0",
    "Variant1",
    "Variant1Spec",
    "Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironment",
    "Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFile",
    "Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileAutomationsFilePathIsThePathToTheAutomationsFileThatIsAppliedInTheEnvironmentRelativeToTheRepoRoot",
    "Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileSession",
    "Variant1SpecContent",
    "Variant1SpecContentContent",
    "Variant1SpecContentContentTheGitEmailAddress",
    "Variant1SpecContentContentTheGitUsername",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitialized",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializer",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpec",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURL",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURLContextURL",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGit",
    "Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGitGit",
    "Variant1SpecContentContentSessionShouldBeChangedToTriggerAContentReinitialization",
    "Variant1SpecDevcontainer",
    "Variant1SpecDevcontainerDevcontainer",
    "Variant1SpecDevcontainerDevcontainerDevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot",
    "Variant1SpecDevcontainerDevcontainerSessionShouldBeChangedToTriggerADevcontainerRebuild",
    "Variant1SpecTimeoutConfiguresTheEnvironmentTimeout",
    "Variant1SpecTimeoutConfiguresTheEnvironmentTimeoutTimeout",
]


class Variant0(TypedDict, total=False):
    metadata: Required[object]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant1(TypedDict, total=False):
    spec: Required[Variant1Spec]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileAutomationsFilePathIsThePathToTheAutomationsFileThatIsAppliedInTheEnvironmentRelativeToTheRepoRoot(
    TypedDict, total=False
):
    automations_file_path: Required[Annotated[str, PropertyInfo(alias="automationsFilePath")]]
    """
    automations_file_path is the path to the automations file that is applied in the
    environment,

    relative to the repo root. path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """


class Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileSession(TypedDict, total=False):
    session: Required[str]


Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFile: TypeAlias = Union[
    Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileAutomationsFilePathIsThePathToTheAutomationsFileThatIsAppliedInTheEnvironmentRelativeToTheRepoRoot,
    Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileSession,
]


class Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironment(TypedDict, total=False):
    automations_file: Required[
        Annotated[
            Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFile,
            PropertyInfo(alias="automationsFile"),
        ]
    ]
    """automations_file is the automations file spec of the environment"""


class Variant1SpecContentContentTheGitEmailAddress(TypedDict, total=False):
    git_email: Required[Annotated[str, PropertyInfo(alias="gitEmail")]]
    """The Git email address"""


class Variant1SpecContentContentTheGitUsername(TypedDict, total=False):
    git_username: Required[Annotated[str, PropertyInfo(alias="gitUsername")]]
    """The Git username"""


class Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURLContextURL(
    TypedDict, total=False
):
    url: str
    """url is the URL from which the environment is created"""


class Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURL(
    TypedDict, total=False
):
    context_url: Required[
        Annotated[
            Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURLContextURL,
            PropertyInfo(alias="contextUrl"),
        ]
    ]


class Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGitGit(
    TypedDict, total=False
):
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


class Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGit(
    TypedDict, total=False
):
    git: Required[
        Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGitGit
    ]


Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpec: TypeAlias = Union[
    Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURL,
    Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGit,
]


class Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializer(
    TypedDict, total=False
):
    specs: Iterable[Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpec]


class Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitialized(TypedDict, total=False):
    initializer: Required[Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializer]
    """EnvironmentInitializer specifies how an environment is to be initialized"""


class Variant1SpecContentContentSessionShouldBeChangedToTriggerAContentReinitialization(TypedDict, total=False):
    session: Required[str]
    """session should be changed to trigger a content reinitialization"""


Variant1SpecContentContent: TypeAlias = Union[
    Variant1SpecContentContentTheGitEmailAddress,
    Variant1SpecContentContentTheGitUsername,
    Variant1SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitialized,
    Variant1SpecContentContentSessionShouldBeChangedToTriggerAContentReinitialization,
]


class Variant1SpecContent(TypedDict, total=False):
    content: Required[Variant1SpecContentContent]


class Variant1SpecDevcontainerDevcontainerDevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot(
    TypedDict, total=False
):
    devcontainer_file_path: Required[Annotated[str, PropertyInfo(alias="devcontainerFilePath")]]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """


class Variant1SpecDevcontainerDevcontainerSessionShouldBeChangedToTriggerADevcontainerRebuild(TypedDict, total=False):
    session: Required[str]
    """session should be changed to trigger a devcontainer rebuild"""


Variant1SpecDevcontainerDevcontainer: TypeAlias = Union[
    Variant1SpecDevcontainerDevcontainerDevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot,
    Variant1SpecDevcontainerDevcontainerSessionShouldBeChangedToTriggerADevcontainerRebuild,
]


class Variant1SpecDevcontainer(TypedDict, total=False):
    devcontainer: Required[Variant1SpecDevcontainerDevcontainer]


class Variant1SpecTimeoutConfiguresTheEnvironmentTimeoutTimeout(TypedDict, total=False):
    disconnected: Required[str]
    """
    A Duration represents a signed, fixed-length span of time represented as a count
    of seconds and fractions of seconds at nanosecond resolution. It is independent
    of any calendar and concepts like "day" or "month". It is related to Timestamp
    in that the difference between two Timestamp values is a Duration and it can be
    added or subtracted from a Timestamp. Range is approximately +-10,000 years.

    # Examples

    Example 1: Compute Duration from two Timestamps in pseudo code.

         Timestamp start = ...;
         Timestamp end = ...;
         Duration duration = ...;

         duration.seconds = end.seconds - start.seconds;
         duration.nanos = end.nanos - start.nanos;

         if (duration.seconds < 0 && duration.nanos > 0) {
           duration.seconds += 1;
           duration.nanos -= 1000000000;
         } else if (duration.seconds > 0 && duration.nanos < 0) {
           duration.seconds -= 1;
           duration.nanos += 1000000000;
         }

    Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.

         Timestamp start = ...;
         Duration duration = ...;
         Timestamp end = ...;

         end.seconds = start.seconds + duration.seconds;
         end.nanos = start.nanos + duration.nanos;

         if (end.nanos < 0) {
           end.seconds -= 1;
           end.nanos += 1000000000;
         } else if (end.nanos >= 1000000000) {
           end.seconds += 1;
           end.nanos -= 1000000000;
         }

    Example 3: Compute Duration from datetime.timedelta in Python.

         td = datetime.timedelta(days=3, minutes=10)
         duration = Duration()
         duration.FromTimedelta(td)

    # JSON Mapping

    In JSON format, the Duration type is encoded as a string rather than an object,
    where the string ends in the suffix "s" (indicating seconds) and is preceded by
    the number of seconds, with nanoseconds expressed as fractional seconds. For
    example, 3 seconds with 0 nanoseconds should be encoded in JSON format as "3s",
    while 3 seconds and 1 nanosecond should be expressed in JSON format as
    "3.000000001s", and 3 seconds and 1 microsecond should be expressed in JSON
    format as "3.000001s".
    """


class Variant1SpecTimeoutConfiguresTheEnvironmentTimeout(TypedDict, total=False):
    timeout: Required[Variant1SpecTimeoutConfiguresTheEnvironmentTimeoutTimeout]
    """Timeout configures the environment timeout"""


Variant1Spec: TypeAlias = Union[
    Variant1SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironment,
    Variant1SpecContent,
    Variant1SpecDevcontainer,
    Variant1SpecTimeoutConfiguresTheEnvironmentTimeout,
]

EnvironmentUpdateParams: TypeAlias = Union[Variant0, Variant1]
