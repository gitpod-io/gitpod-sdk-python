# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    container_registry_basic_auth_host: Annotated[str, PropertyInfo(alias="containerRegistryBasicAuthHost")]
    """
    secret will be mounted as a docker config in the environment VM, mount will have
    the docker registry host
    """

    environment_variable: Annotated[bool, PropertyInfo(alias="environmentVariable")]
    """
    secret will be created as an Environment Variable with the same name as the
    secret
    """

    file_path: Annotated[str, PropertyInfo(alias="filePath")]
    """
    absolute path to the file where the secret is mounted value must be an absolute
    path (start with a /):

    ```
    this.matches('^/(?:[^/]*/)*.*$')
    ```
    """

    name: str

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id is the ProjectID this Secret belongs to"""

    value: str
    """value is the plaintext value of the secret"""
