# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["RecommendedEditors", "Editors"]


class Editors(BaseModel):
    """EditorVersions contains the recommended versions for an editor."""

    versions: Optional[List[str]] = None
    """
    versions is the list of recommended versions for this editor. If empty, all
    available versions are recommended. Examples for JetBrains: ["2025.1", "2024.3"]
    """


class RecommendedEditors(BaseModel):
    """RecommendedEditors contains the map of recommended editors and their versions."""

    editors: Optional[Dict[str, Editors]] = None
    """
    editors maps editor aliases to their recommended versions. Key is the editor
    alias (e.g., "intellij", "goland", "vscode"). Value contains the list of
    recommended versions for that editor. If versions list is empty, all available
    versions are recommended. Example: {"intellij": {versions: ["2025.1",
    "2024.3"]}, "goland": {}}
    """
