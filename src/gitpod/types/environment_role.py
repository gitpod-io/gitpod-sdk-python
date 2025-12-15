# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EnvironmentRole"]

EnvironmentRole: TypeAlias = Literal[
    "ENVIRONMENT_ROLE_UNSPECIFIED", "ENVIRONMENT_ROLE_DEFAULT", "ENVIRONMENT_ROLE_PREBUILD", "ENVIRONMENT_ROLE_WORKFLOW"
]
