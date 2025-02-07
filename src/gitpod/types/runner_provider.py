# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunnerProvider"]

RunnerProvider: TypeAlias = Literal[
    "RUNNER_PROVIDER_UNSPECIFIED",
    "RUNNER_PROVIDER_AWS_EC2",
    "RUNNER_PROVIDER_LINUX_HOST",
    "RUNNER_PROVIDER_DESKTOP_MAC",
]
