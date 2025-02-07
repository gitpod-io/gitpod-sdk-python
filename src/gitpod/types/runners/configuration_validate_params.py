# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from ..._models import set_pydantic_config
from ..shared_params.environment_class import EnvironmentClass

__all__ = ["ConfigurationValidateParams", "ScmIntegration"]


class ConfigurationValidateParams(TypedDict, total=False):
    environment_class: Annotated[EnvironmentClass, PropertyInfo(alias="environmentClass")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_integration: Annotated[ScmIntegration, PropertyInfo(alias="scmIntegration")]


class ScmIntegration(TypedDict, total=False):
    id: str
    """id is the unique identifier of the SCM integration"""

    host: str

    oauth_client_id: Annotated[Optional[str], PropertyInfo(alias="oauthClientId")]
    """
    oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
    configured, oauth_client_secret must also be set.
    """

    oauth_encrypted_client_secret: Annotated[
        Union[str, Base64FileInput], PropertyInfo(alias="oauthEncryptedClientSecret", format="base64")
    ]
    """
    oauth_encrypted_client_secret is the OAuth app's client secret encrypted with
    the runner's public key, if OAuth is configured. This can be used to e.g.
    validate an already encrypted client secret of an existing SCM integration.
    """

    oauth_plaintext_client_secret: Annotated[str, PropertyInfo(alias="oauthPlaintextClientSecret")]
    """
    oauth_plaintext_client_secret is the OAuth app's client secret in clear text, if
    OAuth is configured. This can be set to validate any new client secret before it
    is encrypted and stored. This value will not be stored and get encrypted with
    the runner's public key before passing it to the runner.
    """

    pat: bool

    scm_id: Annotated[str, PropertyInfo(alias="scmId")]
    """
    scm_id references the scm_id in the runner's configuration schema that this
    integration is for
    """


set_pydantic_config(ScmIntegration, {"arbitrary_types_allowed": True})
