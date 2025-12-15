# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PrebuildTrigger"]

PrebuildTrigger: TypeAlias = Literal[
    "PREBUILD_TRIGGER_UNSPECIFIED", "PREBUILD_TRIGGER_MANUAL", "PREBUILD_TRIGGER_SCHEDULED"
]
