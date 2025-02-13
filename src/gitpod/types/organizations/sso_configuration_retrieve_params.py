# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SSOConfigurationRetrieveParams"]


class SSOConfigurationRetrieveParams(TypedDict, total=False):
    sso_configuration_id: Required[Annotated[str, PropertyInfo(alias="ssoConfigurationId")]]
    """sso_configuration_id is the ID of the SSO configuration to get"""
