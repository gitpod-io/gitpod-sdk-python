# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Editor"]


class Editor(BaseModel):
    id: str

    installation_instructions: str = FieldInfo(alias="installationInstructions")

    name: str

    url_template: str = FieldInfo(alias="urlTemplate")

    alias: Optional[str] = None

    icon_url: Optional[str] = FieldInfo(alias="iconUrl", default=None)

    short_description: Optional[str] = FieldInfo(alias="shortDescription", default=None)
