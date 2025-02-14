# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Editor"]


class Editor(BaseModel):
    id: str

    alias: str

    icon_url: str = FieldInfo(alias="iconUrl")

    installation_instructions: str = FieldInfo(alias="installationInstructions")

    name: str

    short_description: str = FieldInfo(alias="shortDescription")

    url_template: str = FieldInfo(alias="urlTemplate")
