# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .admission_level import AdmissionLevel
from .environment_initializer_param import EnvironmentInitializerParam

__all__ = [
    "EnvironmentUpdateParams",
    "Spec",
    "SpecAutomationsFile",
    "SpecContent",
    "SpecDevcontainer",
    "SpecPort",
    "SpecSSHPublicKey",
    "SpecTimeout",
]


class EnvironmentUpdateParams(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """environment_id specifies which environment should be updated.

    +required
    """

    metadata: Optional[object]

    spec: Optional[Spec]


class SpecAutomationsFile(TypedDict, total=False):
    automations_file_path: Annotated[Optional[str], PropertyInfo(alias="automationsFilePath")]
    """
    automations_file_path is the path to the automations file that is applied in the
    environment, relative to the repo root. path must not be absolute (start with a
    /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    session: Optional[str]


class SpecContent(TypedDict, total=False):
    git_email: Annotated[Optional[str], PropertyInfo(alias="gitEmail")]
    """The Git email address"""

    git_username: Annotated[Optional[str], PropertyInfo(alias="gitUsername")]
    """The Git username"""

    initializer: Optional[EnvironmentInitializerParam]
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    session: Optional[str]
    """session should be changed to trigger a content reinitialization"""


class SpecDevcontainer(TypedDict, total=False):
    devcontainer_file_path: Annotated[Optional[str], PropertyInfo(alias="devcontainerFilePath")]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    session: Optional[str]
    """session should be changed to trigger a devcontainer rebuild"""


class SpecPort(TypedDict, total=False):
    admission: AdmissionLevel
    """Admission level describes who can access an environment instance and its ports."""

    name: str
    """name of this port"""

    port: int
    """port number"""


class SpecSSHPublicKey(TypedDict, total=False):
    id: str
    """id is the unique identifier of the public key"""

    value: Optional[str]
    """
    value is the actual public key in the public key file format if not provided,
    the public key will be removed
    """


class SpecTimeout(TypedDict, total=False):
    disconnected: Optional[str]
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
    automations_file: Annotated[Optional[SpecAutomationsFile], PropertyInfo(alias="automationsFile")]
    """automations_file is the automations file spec of the environment"""

    content: Optional[SpecContent]

    devcontainer: Optional[SpecDevcontainer]

    ports: Iterable[SpecPort]
    """ports controls port sharing"""

    ssh_public_keys: Annotated[Iterable[SpecSSHPublicKey], PropertyInfo(alias="sshPublicKeys")]
    """
    ssh_public_keys are the public keys to update empty array means nothing to
    update
    """

    timeout: Optional[SpecTimeout]
    """Timeout configures the environment timeout"""
