# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .gateway_info import GatewayInfo
from .runner_phase import RunnerPhase
from .runner_capability import RunnerCapability
from .shared.field_value import FieldValue

__all__ = ["RunnerStatus"]


class RunnerStatus(BaseModel):
    """RunnerStatus represents the status of a runner"""

    additional_info: Optional[List[FieldValue]] = FieldInfo(alias="additionalInfo", default=None)
    """additional_info contains additional information about the runner, e.g.

    a CloudFormation stack URL.
    """

    capabilities: Optional[List[RunnerCapability]] = None
    """capabilities is a list of capabilities the runner supports."""

    gateway_info: Optional[GatewayInfo] = FieldInfo(alias="gatewayInfo", default=None)
    """gateway_info is information about the gateway to which the runner is connected."""

    llm_url: Optional[str] = FieldInfo(alias="llmUrl", default=None)
    """llm_url is the URL of the LLM service to which the runner is connected."""

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)

    message: Optional[str] = None
    """
    The runner's reported message which is shown to users. This message adds more
    context to the runner's phase.
    """

    phase: Optional[RunnerPhase] = None
    """The runner's reported phase"""

    public_key: Optional[str] = FieldInfo(alias="publicKey", default=None)
    """public_key is the runner's public key used for encryption (32 bytes)"""

    region: Optional[str] = None
    """region is the region the runner is running in, if applicable."""

    support_bundle_url: Optional[str] = FieldInfo(alias="supportBundleUrl", default=None)
    """
    support_bundle_url is the URL at which the runner support bundle can be
    accessed. This URL provides access to pprof profiles and other debug
    information. Only available for standalone runners.
    """

    system_details: Optional[str] = FieldInfo(alias="systemDetails", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time when the status was last updated."""

    version: Optional[str] = None
