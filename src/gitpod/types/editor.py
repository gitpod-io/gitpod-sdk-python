# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Editor"]


class Editor(BaseModel):
    id: Optional[str] = None

    alias: Optional[str] = None

    icon_url: Optional[str] = FieldInfo(alias="iconUrl", default=None)

    installation_instructions: Optional[str] = FieldInfo(alias="installationInstructions", default=None)

    name: Optional[str] = None

    short_description: Optional[str] = FieldInfo(alias="shortDescription", default=None)

    url_template: Optional[str] = FieldInfo(alias="urlTemplate", default=None)
