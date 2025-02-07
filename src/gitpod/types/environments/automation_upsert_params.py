# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .automations_file_param import AutomationsFileParam

__all__ = ["AutomationUpsertParams"]


class AutomationUpsertParams(TypedDict, total=False):
    automations_file: Annotated[AutomationsFileParam, PropertyInfo(alias="automationsFile")]
    """
    WARN: Do not remove any field here, as it will break reading automation yaml
    files. We error if there are any unknown fields in the yaml (to ensure the yaml
    is correct), but would break if we removed any fields. This includes marking a
    field as "reserved" in the proto file, this will also break reading the yaml.
    """

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
