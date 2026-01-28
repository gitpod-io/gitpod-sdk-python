# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScimConfigurationRegenerateTokenParams"]


class ScimConfigurationRegenerateTokenParams(TypedDict, total=False):
    scim_configuration_id: Required[Annotated[str, PropertyInfo(alias="scimConfigurationId")]]
    """
    scim_configuration_id is the ID of the SCIM configuration to regenerate token
    for
    """

    token_expires_in: Annotated[Optional[str], PropertyInfo(alias="tokenExpiresIn")]
    """
    token_expires_in is the duration until the new token expires. If not specified,
    uses the same duration as the previous token.
    """
