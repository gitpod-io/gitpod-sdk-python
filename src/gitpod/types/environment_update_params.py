# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EnvironmentUpdateParams",
    "Spec",
    "SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironment",
    "SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFile",
    "SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileAutomationsFilePathIsThePathToTheAutomationsFileThatIsAppliedInTheEnvironmentRelativeToTheRepoRoot",
    "SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileSession",
    "SpecContent",
    "SpecContentContent",
    "SpecContentContentTheGitEmailAddress",
    "SpecContentContentTheGitUsername",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitialized",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializer",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpec",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURL",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURLContextURL",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGit",
    "SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGitGit",
    "SpecContentContentSessionShouldBeChangedToTriggerAContentReinitialization",
    "SpecDevcontainer",
    "SpecDevcontainerDevcontainer",
    "SpecDevcontainerDevcontainerDevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot",
    "SpecDevcontainerDevcontainerSessionShouldBeChangedToTriggerADevcontainerRebuild",
    "SpecTimeoutConfiguresTheEnvironmentTimeout",
    "SpecTimeoutConfiguresTheEnvironmentTimeoutTimeout",
]


class EnvironmentUpdateParams(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """environment_id specifies which environment should be updated.

    +required
    """

    metadata: Optional[object]

    spec: Optional[Spec]


class SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileAutomationsFilePathIsThePathToTheAutomationsFileThatIsAppliedInTheEnvironmentRelativeToTheRepoRoot(
    TypedDict, total=False
):
    automations_file_path: Required[Annotated[str, PropertyInfo(alias="automationsFilePath")]]
    """
    automations_file_path is the path to the automations file that is applied in the
    environment, relative to the repo root. path must not be absolute (start with a
    /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """


class SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileSession(TypedDict, total=False):
    session: Required[str]


SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFile: TypeAlias = Union[
    SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileAutomationsFilePathIsThePathToTheAutomationsFileThatIsAppliedInTheEnvironmentRelativeToTheRepoRoot,
    SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFileSession,
]


class SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironment(TypedDict, total=False):
    automations_file: Required[
        Annotated[
            SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironmentAutomationsFile,
            PropertyInfo(alias="automationsFile"),
        ]
    ]
    """automations_file is the automations file spec of the environment"""


class SpecContentContentTheGitEmailAddress(TypedDict, total=False):
    git_email: Required[Annotated[str, PropertyInfo(alias="gitEmail")]]
    """The Git email address"""


class SpecContentContentTheGitUsername(TypedDict, total=False):
    git_username: Required[Annotated[str, PropertyInfo(alias="gitUsername")]]
    """The Git username"""


class SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURLContextURL(
    TypedDict, total=False
):
    url: str
    """url is the URL from which the environment is created"""


class SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURL(
    TypedDict, total=False
):
    context_url: Required[
        Annotated[
            SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURLContextURL,
            PropertyInfo(alias="contextUrl"),
        ]
    ]


class SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGitGit(
    TypedDict, total=False
):
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


class SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGit(
    TypedDict, total=False
):
    git: Required[SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGitGit]


SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpec: TypeAlias = Union[
    SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecContextURL,
    SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpecGit,
]


class SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializer(TypedDict, total=False):
    specs: Iterable[SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializerSpec]


class SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitialized(TypedDict, total=False):
    initializer: Required[SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitializedInitializer]
    """EnvironmentInitializer specifies how an environment is to be initialized"""


class SpecContentContentSessionShouldBeChangedToTriggerAContentReinitialization(TypedDict, total=False):
    session: Required[str]
    """session should be changed to trigger a content reinitialization"""


SpecContentContent: TypeAlias = Union[
    SpecContentContentTheGitEmailAddress,
    SpecContentContentTheGitUsername,
    SpecContentContentInitializerConfiguresHowTheEnvironmentIsToBeInitialized,
    SpecContentContentSessionShouldBeChangedToTriggerAContentReinitialization,
]


class SpecContent(TypedDict, total=False):
    content: Required[SpecContentContent]


class SpecDevcontainerDevcontainerDevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot(
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


class SpecDevcontainerDevcontainerSessionShouldBeChangedToTriggerADevcontainerRebuild(TypedDict, total=False):
    session: Required[str]
    """session should be changed to trigger a devcontainer rebuild"""


SpecDevcontainerDevcontainer: TypeAlias = Union[
    SpecDevcontainerDevcontainerDevcontainerFilePathIsThePathToTheDevcontainerFileRelativeToTheRepoRoot,
    SpecDevcontainerDevcontainerSessionShouldBeChangedToTriggerADevcontainerRebuild,
]


class SpecDevcontainer(TypedDict, total=False):
    devcontainer: Required[SpecDevcontainerDevcontainer]


class SpecTimeoutConfiguresTheEnvironmentTimeoutTimeout(TypedDict, total=False):
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


class SpecTimeoutConfiguresTheEnvironmentTimeout(TypedDict, total=False):
    timeout: Required[SpecTimeoutConfiguresTheEnvironmentTimeoutTimeout]
    """Timeout configures the environment timeout"""


Spec: TypeAlias = Union[
    SpecAutomationsFileIsTheAutomationsFileSpecOfTheEnvironment,
    SpecContent,
    SpecDevcontainer,
    SpecTimeoutConfiguresTheEnvironmentTimeout,
]
