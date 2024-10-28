# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerInteractionGetLatestVersionResponse"]


class RunnerInteractionGetLatestVersionResponse(BaseModel):
    auto_update: Optional[bool] = FieldInfo(alias="autoUpdate", default=None)
    """auto-update indicates if the runner should be updated automatically"""

    gitpod_cli_download_url: Optional[str] = FieldInfo(alias="gitpodCliDownloadUrl", default=None)
    """gitpod_cli_download_url is the URL to download the gitpod CLI"""

    runner_image: Optional[str] = FieldInfo(alias="runnerImage", default=None)
    """The container image of the runner"""

    supervisor_download_url: Optional[str] = FieldInfo(alias="supervisorDownloadUrl", default=None)
    """supervisor_download_url is the URL to download the supervisor"""

    version: Optional[str] = None
    """The latest version of the runner"""
