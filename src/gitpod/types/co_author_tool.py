# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CoAuthorTool"]

CoAuthorTool: TypeAlias = Literal[
    "CO_AUTHOR_TOOL_UNSPECIFIED",
    "CO_AUTHOR_TOOL_NO_COAUTHOR",
    "CO_AUTHOR_TOOL_HUMAN_COAUTHOR",
    "CO_AUTHOR_TOOL_ONA",
    "CO_AUTHOR_TOOL_GITHUB_COPILOT",
    "CO_AUTHOR_TOOL_CURSOR",
    "CO_AUTHOR_TOOL_OTHER",
    "CO_AUTHOR_TOOL_CLAUDE",
    "CO_AUTHOR_TOOL_CODEX",
]
