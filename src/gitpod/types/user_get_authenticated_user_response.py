# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .user import User
from .._models import BaseModel

__all__ = ["UserGetAuthenticatedUserResponse"]


class UserGetAuthenticatedUserResponse(BaseModel):
    user: User
