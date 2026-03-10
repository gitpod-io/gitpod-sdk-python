# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .type import Type

__all__ = ["AgentMessageParam"]


class AgentMessageParam(TypedDict, total=False):
    """AgentMessage is a message sent between agents (e.g.

    from a parent agent to a
     child agent execution, or vice versa).
    """

    payload: str
    """Free-form payload of the message."""

    type: Type
