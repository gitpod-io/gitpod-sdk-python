# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunnerCapability"]

RunnerCapability: TypeAlias = Literal[
    "RUNNER_CAPABILITY_UNSPECIFIED",
    "RUNNER_CAPABILITY_FETCH_LOCAL_SCM_INTEGRATIONS",
    "RUNNER_CAPABILITY_SECRET_CONTAINER_REGISTRY",
]
