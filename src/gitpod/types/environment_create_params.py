# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EnvironmentCreateParams",
    "Spec",
    "SpecAutomationsFile",
    "SpecContent",
    "SpecContentInitializer",
    "SpecContentInitializerSpec",
    "SpecDevcontainer",
    "SpecMachine",
    "SpecPort",
    "SpecSecret",
    "SpecSSHPublicKey",
    "SpecTimeout",
]


class EnvironmentCreateParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    spec: Spec
    """EnvironmentSpec specifies the configuration of an environment for an environment

    start
    """

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class SpecAutomationsFile(TypedDict, total=False):
    automations_file_path: Annotated[str, PropertyInfo(alias="automationsFilePath")]
    """
    automations_file_path is the path to the automations file that is applied in the
    environment,

    relative to the repo root. path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    session: str


class SpecContentInitializerSpec:
    pass


class SpecContentInitializer(TypedDict, total=False):
    specs: Iterable[SpecContentInitializerSpec]


class SpecContent(TypedDict, total=False):
    git_email: Annotated[str, PropertyInfo(alias="gitEmail")]
    """The Git email address"""

    git_username: Annotated[str, PropertyInfo(alias="gitUsername")]
    """The Git username"""

    initializer: SpecContentInitializer
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    session: str


class SpecDevcontainer(TypedDict, total=False):
    devcontainer_file_path: Annotated[str, PropertyInfo(alias="devcontainerFilePath")]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    session: str


_SpecMachineReservedKeywords = TypedDict(
    "_SpecMachineReservedKeywords",
    {
        "class": str,
    },
    total=False,
)


class SpecMachine(_SpecMachineReservedKeywords, total=False):
    session: str


class SpecPort(TypedDict, total=False):
    admission: Literal["ADMISSION_LEVEL_UNSPECIFIED", "ADMISSION_LEVEL_OWNER_ONLY", "ADMISSION_LEVEL_EVERYONE"]
    """Admission level describes who can access an environment instance and its ports."""

    name: str
    """name of this port"""

    port: int
    """port number"""


class SpecSecret:
    pass


class SpecSSHPublicKey(TypedDict, total=False):
    id: str
    """id is the unique identifier of the public key"""

    value: str
    """value is the actual public key in the public key file format"""


class SpecTimeout(TypedDict, total=False):
    disconnected: str
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


class Spec(TypedDict, total=False):
    admission: Literal["ADMISSION_LEVEL_UNSPECIFIED", "ADMISSION_LEVEL_OWNER_ONLY", "ADMISSION_LEVEL_EVERYONE"]
    """Admission level describes who can access an environment instance and its ports."""

    automations_file: Annotated[SpecAutomationsFile, PropertyInfo(alias="automationsFile")]
    """automations_file is the automations file spec of the environment"""

    content: SpecContent
    """content is the content spec of the environment"""

    desired_phase: Annotated[
        Literal[
            "ENVIRONMENT_PHASE_UNSPECIFIED",
            "ENVIRONMENT_PHASE_CREATING",
            "ENVIRONMENT_PHASE_STARTING",
            "ENVIRONMENT_PHASE_RUNNING",
            "ENVIRONMENT_PHASE_UPDATING",
            "ENVIRONMENT_PHASE_STOPPING",
            "ENVIRONMENT_PHASE_STOPPED",
            "ENVIRONMENT_PHASE_DELETING",
            "ENVIRONMENT_PHASE_DELETED",
        ],
        PropertyInfo(alias="desiredPhase"),
    ]
    """Phase is the desired phase of the environment"""

    devcontainer: SpecDevcontainer
    """devcontainer is the devcontainer spec of the environment"""

    machine: SpecMachine
    """machine is the machine spec of the environment"""

    ports: Iterable[SpecPort]
    """ports is the set of ports which ought to be exposed to the internet"""

    secrets: Iterable[SpecSecret]
    """secrets are confidential data that is mounted into the environment"""

    spec_version: Annotated[str, PropertyInfo(alias="specVersion")]
    """version of the spec.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.spec_version <
    b.spec_version then a was the spec before b.
    """

    ssh_public_keys: Annotated[Iterable[SpecSSHPublicKey], PropertyInfo(alias="sshPublicKeys")]
    """ssh_public_keys are the public keys used to ssh into the environment"""

    timeout: SpecTimeout
    """Timeout configures the environment timeout"""
