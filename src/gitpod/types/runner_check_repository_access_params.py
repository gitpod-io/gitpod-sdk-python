# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerCheckRepositoryAccessParams"]


class RunnerCheckRepositoryAccessParams(TypedDict, total=False):
    repository_url: Annotated[str, PropertyInfo(alias="repositoryUrl")]
    """
    repository_url is the URL of the repository to check access for. Can be a clone
    URL (https://github.com/org/repo.git) or web URL (https://github.com/org/repo).
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
