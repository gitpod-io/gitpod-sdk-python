# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RunnerInteractionUpdateRunnerConfigurationSchemaParams",
    "ConfigSchema",
    "ConfigSchemaScm",
    "ConfigSchemaScmOAuth",
    "ConfigSchemaScmPat",
]


class RunnerInteractionUpdateRunnerConfigurationSchemaParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    config_schema: Annotated[ConfigSchema, PropertyInfo(alias="configSchema")]
    """config_schema is the schema for the runner's configuration"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """The runner's identity"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class ConfigSchemaScmOAuth(TypedDict, total=False):
    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """
    callback_url is the URL the OAuth app will redirect to after the user has
    authenticated.
    """


class ConfigSchemaScmPat(TypedDict, total=False):
    description: str
    """description is a human-readable description of the PAT."""

    docs_link: Annotated[str, PropertyInfo(alias="docsLink")]
    """
    docs_link is a link to the documentation on how to create a PAT for this SCM
    system.
    """


class ConfigSchemaScm(TypedDict, total=False):
    default_hosts: Annotated[List[str], PropertyInfo(alias="defaultHosts")]

    name: str

    oauth: ConfigSchemaScmOAuth

    pat: ConfigSchemaScmPat

    scm_id: Annotated[str, PropertyInfo(alias="scmId")]


class ConfigSchema(TypedDict, total=False):
    environment_classes: Annotated[
        Iterable[Union[object, object, object, object, object, object]], PropertyInfo(alias="environmentClasses")
    ]

    runner_config: Annotated[
        Iterable[Union[object, object, object, object, object, object]], PropertyInfo(alias="runnerConfig")
    ]

    scm: Iterable[ConfigSchemaScm]

    version: str
    """The schema version"""
