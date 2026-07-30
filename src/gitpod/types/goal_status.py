# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["GoalStatus"]

GoalStatus: TypeAlias = Literal[
    "GOAL_STATUS_UNSPECIFIED",
    "GOAL_STATUS_ACTIVE",
    "GOAL_STATUS_PAUSED",
    "GOAL_STATUS_COMPLETED",
    "GOAL_STATUS_BUDGET_EXHAUSTED",
    "GOAL_STATUS_BLOCKED",
    "GOAL_STATUS_USAGE_LIMITED",
]
