# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .secret_scope_param import SecretScopeParam

__all__ = ["SecretCreateParams", "CredentialProxy", "Source", "SourceOidcJfrog"]


class SecretCreateParams(TypedDict, total=False):
    api_only: Annotated[bool, PropertyInfo(alias="apiOnly")]
    """
    api_only indicates the secret is only available via API/CLI. These secrets are
    NOT automatically injected into services or devcontainers. Useful for secrets
    that should only be consumed programmatically (e.g., by security agents).
    """

    container_registry_basic_auth_host: Annotated[str, PropertyInfo(alias="containerRegistryBasicAuthHost")]
    """
    secret will be mounted as a docker config in the environment VM, mount will have
    the docker registry host
    """

    credential_proxy: Annotated[CredentialProxy, PropertyInfo(alias="credentialProxy")]
    """
    credential_proxy configures transparent credential injection when environments
    materialize this secret. When set, the credential proxy intercepts HTTPS traffic
    to the target hosts and replaces the dummy mounted value with the real value in
    the specified HTTP header. The real secret value is never exposed in the
    environment. This field is orthogonal to mount — a secret can be both mounted
    and proxied at the same time.
    """

    environment_variable: Annotated[bool, PropertyInfo(alias="environmentVariable")]
    """
    secret will be created as an Environment Variable with the same name as the
    secret
    """

    file_path: Annotated[str, PropertyInfo(alias="filePath")]
    """
    absolute path to the file where the secret is mounted value must be an absolute
    path (e.g. /path/to/file):

    ```
    this.matches('^/[^/].*$')
    ```
    """

    name: str

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """
    project_id is the ProjectID this Secret belongs to Deprecated: use scope instead
    """

    scope: SecretScopeParam
    """scope is the scope of the secret"""

    source: Source
    """source is the source of the secret, possibly verbatim value"""

    value: str
    """value is the plaintext value of the secret.

    When set, source must be unset or verbatim.
    """


class CredentialProxy(TypedDict, total=False):
    """
    credential_proxy configures transparent credential injection when
     environments materialize this secret. When set, the credential proxy
     intercepts HTTPS traffic to the target hosts and replaces the dummy
     mounted value with the real value in the specified HTTP header. The real
     secret value is never exposed in the environment.
     This field is orthogonal to mount — a secret can be both mounted and
     proxied at the same time.
    """

    header: str
    """header is the HTTP header name to inject (e.g. "Authorization")."""

    target_hosts: Annotated[SequenceNotStr[str], PropertyInfo(alias="targetHosts")]
    """
    target_hosts lists the hostnames to intercept (for example "github.com" or
    "\\**.github.com"). Wildcards are subdomain-only and do not match the apex domain.
    """


class SourceOidcJfrog(TypedDict, total=False):
    host: str
    """host must be a hostname or IP address with optional port:

    ```
    this.matches("^([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?[.])*[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?(:([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?$")
    ```
    """

    provider_name: Annotated[str, PropertyInfo(alias="providerName")]


class Source(TypedDict, total=False):
    """source is the source of the secret, possibly verbatim value"""

    oidc_jfrog: Annotated[SourceOidcJfrog, PropertyInfo(alias="oidcJfrog")]

    verbatim: bool
