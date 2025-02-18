# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .admission_level import AdmissionLevel
from .environment_phase import EnvironmentPhase
from .environment_initializer import EnvironmentInitializer

__all__ = [
    "EnvironmentSpec",
    "AutomationsFile",
    "Content",
    "Devcontainer",
    "DevcontainerDotfiles",
    "Machine",
    "Port",
    "Secret",
    "SSHPublicKey",
    "Timeout",
]


class AutomationsFile(BaseModel):
    automations_file_path: Optional[str] = FieldInfo(alias="automationsFilePath", default=None)
    """
    automations_file_path is the path to the automations file that is applied in the
    environment, relative to the repo root. path must not be absolute (start with a
    /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    session: Optional[str] = None


class Content(BaseModel):
    git_email: Optional[str] = FieldInfo(alias="gitEmail", default=None)
    """The Git email address"""

    git_username: Optional[str] = FieldInfo(alias="gitUsername", default=None)
    """The Git username"""

    initializer: Optional[EnvironmentInitializer] = None
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    session: Optional[str] = None


class DevcontainerDotfiles(BaseModel):
    repository: str
    """URL of a dotfiles Git repository (e.g. https://github.com/owner/repository)"""

    install_command: Optional[str] = FieldInfo(alias="installCommand", default=None)
    """install_command is the command to run after cloning the dotfiles repository.

    Defaults to run the first file of `install.sh`, `install`, `bootstrap.sh`,
    `bootstrap`, `setup.sh` and `setup` found in the dotfiles repository's root
    folder.
    """

    target_path: Optional[str] = FieldInfo(alias="targetPath", default=None)
    """target_path is the path to clone the dotfiles repository to.

    Defaults to `~/dotfiles`.
    """


class Devcontainer(BaseModel):
    devcontainer_file_path: Optional[str] = FieldInfo(alias="devcontainerFilePath", default=None)
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    dotfiles: Optional[DevcontainerDotfiles] = None
    """Experimental: dotfiles is the dotfiles configuration of the devcontainer"""

    session: Optional[str] = None


class Machine(BaseModel):
    class_: Optional[str] = FieldInfo(alias="class", default=None)
    """Class denotes the class of the environment we ought to start"""

    session: Optional[str] = None


class Port(BaseModel):
    admission: Optional[AdmissionLevel] = None
    """Admission level describes who can access an environment instance and its ports."""

    name: Optional[str] = None
    """name of this port"""

    port: Optional[int] = None
    """port number"""


class Secret(BaseModel):
    container_registry_basic_auth_host: Optional[str] = FieldInfo(alias="containerRegistryBasicAuthHost", default=None)
    """
    container_registry_basic_auth_host is the hostname of the container registry
    that supports basic auth
    """

    environment_variable: Optional[str] = FieldInfo(alias="environmentVariable", default=None)

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """file_path is the path inside the devcontainer where the secret is mounted"""

    git_credential_host: Optional[str] = FieldInfo(alias="gitCredentialHost", default=None)

    name: Optional[str] = None
    """name is the human readable description of the secret"""

    session: Optional[str] = None
    """
    session indicated the current session of the secret. When the session does not
    change, secrets are not reloaded in the environment.
    """

    source: Optional[str] = None
    """source is the source of the secret, for now control-plane or runner"""

    source_ref: Optional[str] = FieldInfo(alias="sourceRef", default=None)
    """source_ref into the source, in case of control-plane this is uuid of the secret"""


class SSHPublicKey(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the public key"""

    value: Optional[str] = None
    """value is the actual public key in the public key file format"""


class Timeout(BaseModel):
    disconnected: Optional[str] = None
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


class EnvironmentSpec(BaseModel):
    admission: Optional[AdmissionLevel] = None
    """Admission level describes who can access an environment instance and its ports."""

    automations_file: Optional[AutomationsFile] = FieldInfo(alias="automationsFile", default=None)
    """automations_file is the automations file spec of the environment"""

    content: Optional[Content] = None
    """content is the content spec of the environment"""

    desired_phase: Optional[EnvironmentPhase] = FieldInfo(alias="desiredPhase", default=None)
    """Phase is the desired phase of the environment"""

    devcontainer: Optional[Devcontainer] = None
    """devcontainer is the devcontainer spec of the environment"""

    machine: Optional[Machine] = None
    """machine is the machine spec of the environment"""

    ports: Optional[List[Port]] = None
    """ports is the set of ports which ought to be exposed to the internet"""

    secrets: Optional[List[Secret]] = None
    """secrets are confidential data that is mounted into the environment"""

    spec_version: Optional[str] = FieldInfo(alias="specVersion", default=None)
    """version of the spec.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.spec_version <
    b.spec_version then a was the spec before b.
    """

    ssh_public_keys: Optional[List[SSHPublicKey]] = FieldInfo(alias="sshPublicKeys", default=None)
    """ssh_public_keys are the public keys used to ssh into the environment"""

    timeout: Optional[Timeout] = None
    """Timeout configures the environment timeout"""
