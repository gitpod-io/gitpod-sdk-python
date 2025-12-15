# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ServiceRole"]

ServiceRole: TypeAlias = Literal[
    "SERVICE_ROLE_UNSPECIFIED",
    "SERVICE_ROLE_DEFAULT",
    "SERVICE_ROLE_EDITOR",
    "SERVICE_ROLE_AI_AGENT",
    "SERVICE_ROLE_SECURITY_AGENT",
]
