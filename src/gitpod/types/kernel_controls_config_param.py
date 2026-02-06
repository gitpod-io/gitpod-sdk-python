# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .veto_param import VetoParam

__all__ = ["KernelControlsConfigParam"]


class KernelControlsConfigParam(TypedDict, total=False):
    """KernelControlsConfig configures kernel-level controls for the environment"""

    veto: VetoParam
    """veto controls blocking mechanisms"""
