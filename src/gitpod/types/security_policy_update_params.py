# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecurityPolicyUpdateParams", "Metadata", "Spec", "SpecExecutables", "SpecExecutablesRule"]


class SecurityPolicyUpdateParams(TypedDict, total=False):
    metadata: Metadata

    security_policy_id: Annotated[str, PropertyInfo(alias="securityPolicyId")]

    spec: Spec
    """Mandate/deploy security agents, e.g.

    CrowdStrike. Mandate credential security/proxy use. These can be modeled later
    as explicit fields if needed.
    """


class Metadata(TypedDict, total=False):
    name: str


class SpecExecutablesRule(TypedDict, total=False):
    effect: Literal["EFFECT_UNSPECIFIED", "EFFECT_ALLOW", "EFFECT_BLOCK", "EFFECT_AUDIT"]
    """effect must be EFFECT_AUDIT or EFFECT_BLOCK.

    EFFECT_ALLOW is not supported on an executable rule.
    """

    path: str
    """
    path is either an absolute executable path, such as /usr/bin/curl, or a bare
    executable name, such as npx. Bare names are expanded by runtime discovery.
    Surrounding whitespace is ignored. Empty or whitespace-only selectors and
    relative paths with directory separators are invalid. Enforcement uses
    executable content hashes, so different paths with identical content share one
    runtime decision and block wins conflicts.
    """


class SpecExecutables(TypedDict, total=False):
    """executables is the public Veto Exec GA policy surface."""

    default_effect: Annotated[
        Literal["EFFECT_UNSPECIFIED", "EFFECT_ALLOW", "EFFECT_BLOCK", "EFFECT_AUDIT"],
        PropertyInfo(alias="defaultEffect"),
    ]
    """
    default_effect controls executables that do not match a rule. For Veto Exec,
    omit this field or set it to EFFECT_ALLOW. EFFECT_UNSPECIFIED is normalized to
    EFFECT_ALLOW.
    """

    rules: Iterable[SpecExecutablesRule]
    """rules contains executable-specific audit or block decisions."""


class Spec(TypedDict, total=False):
    """Mandate/deploy security agents, e.g.

    CrowdStrike.
     Mandate credential security/proxy use.
     These can be modeled later as explicit fields if needed.
    """

    executables: SpecExecutables
    """executables is the public Veto Exec GA policy surface."""
