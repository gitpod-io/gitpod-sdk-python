# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .admission_level import AdmissionLevel
from .environment_initializer_param import EnvironmentInitializerParam

__all__ = [
    "EnvironmentUpdateParams",
    "Metadata",
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

    metadata: Optional[Metadata]

    spec: Optional[Spec]


class Metadata(TypedDict, total=False):
    name: Optional[str]
    """name is the user-defined display name of the environment"""


class SpecAutomationsFile(TypedDict, total=False):
    """automations_file is the automations file spec of the environment"""

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
    """initializer configures how the environment is to be initialized"""

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
    """policy of this port"""

    name: str
    """name of this port"""

    port: int
    """port number"""

    protocol: Literal["PROTOCOL_UNSPECIFIED", "PROTOCOL_HTTP", "PROTOCOL_HTTPS"]
    """
    protocol for communication (Gateway proxy → user environment service). this
    setting only affects the protocol used between Gateway and user environment
    services.
    """


class SpecSSHPublicKey(TypedDict, total=False):
    id: str
    """id is the unique identifier of the public key"""

    value: Optional[str]
    """
    value is the actual public key in the public key file format if not provided,
    the public key will be removed
    """


class SpecTimeout(TypedDict, total=False):
    """Timeout configures the environment timeout"""

    disconnected: Optional[str]
    """
    inacitivity is the maximum time of disconnection before the environment is
    stopped or paused. Minimum duration is 30 minutes. Set to 0 to disable.
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
