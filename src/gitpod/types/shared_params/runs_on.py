# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RunsOn", "Docker"]


class Docker(TypedDict, total=False):
    environment: List[str]

    image: str


class RunsOn(TypedDict, total=False):
    docker: Required[Docker]
