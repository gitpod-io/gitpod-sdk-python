# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["RecommendedEditorsParam", "Editors"]


class Editors(TypedDict, total=False):
    """EditorVersions contains the recommended versions for an editor."""

    versions: SequenceNotStr[str]
    """
    versions is the list of recommended versions for this editor. If empty, all
    available versions are recommended. Examples for JetBrains: ["2025.1", "2024.3"]
    """


class RecommendedEditorsParam(TypedDict, total=False):
    """RecommendedEditors contains the map of recommended editors and their versions."""

    editors: Dict[str, Editors]
    """
    editors maps editor aliases to their recommended versions. Key is the editor
    alias (e.g., "intellij", "goland", "vscode"). Value contains the list of
    recommended versions for that editor. If versions list is empty, all available
    versions are recommended. Example: {"intellij": {versions: ["2025.1",
    "2024.3"]}, "goland": {}}
    """
