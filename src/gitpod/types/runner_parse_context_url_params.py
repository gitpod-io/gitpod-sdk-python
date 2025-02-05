# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerParseContextURLParams"]


class RunnerParseContextURLParams(TypedDict, total=False):
    context_url: Annotated[str, PropertyInfo(alias="contextUrl")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
