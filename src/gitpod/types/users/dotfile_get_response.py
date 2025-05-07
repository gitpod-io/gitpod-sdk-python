# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .dotfiles_configuration import DotfilesConfiguration

__all__ = ["DotfileGetResponse"]


class DotfileGetResponse(BaseModel):
    dotfiles_configuration: DotfilesConfiguration = FieldInfo(alias="dotfilesConfiguration")
