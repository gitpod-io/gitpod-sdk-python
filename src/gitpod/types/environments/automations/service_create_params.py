# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .service_spec_param import ServiceSpecParam
from .service_metadata_param import ServiceMetadataParam

__all__ = ["ServiceCreateParams"]


class ServiceCreateParams(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    metadata: ServiceMetadataParam

    spec: ServiceSpecParam
