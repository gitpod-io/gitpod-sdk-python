# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountGetSSOLoginURLResponse"]


class AccountGetSSOLoginURLResponse(BaseModel):
    login_url: str = FieldInfo(alias="loginUrl")
    """login_url is the URL to redirect the user to for SSO login"""
