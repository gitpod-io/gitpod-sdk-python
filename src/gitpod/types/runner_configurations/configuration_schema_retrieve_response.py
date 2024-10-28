# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConfigurationSchemaRetrieveResponse", "Schema", "SchemaScm", "SchemaScmOAuth", "SchemaScmPat"]


class SchemaScmOAuth(BaseModel):
    callback_url: Optional[str] = FieldInfo(alias="callbackUrl", default=None)
    """
    callback_url is the URL the OAuth app will redirect to after the user has
    authenticated.
    """


class SchemaScmPat(BaseModel):
    description: Optional[str] = None
    """description is a human-readable description of the PAT."""

    docs_link: Optional[str] = FieldInfo(alias="docsLink", default=None)
    """
    docs_link is a link to the documentation on how to create a PAT for this SCM
    system.
    """


class SchemaScm(BaseModel):
    default_hosts: Optional[List[str]] = FieldInfo(alias="defaultHosts", default=None)

    name: Optional[str] = None

    oauth: Optional[SchemaScmOAuth] = None

    pat: Optional[SchemaScmPat] = None

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)


class Schema(BaseModel):
    environment_classes: Optional[List[Union[object, object, object, object, object, object]]] = FieldInfo(
        alias="environmentClasses", default=None
    )

    runner_config: Optional[List[Union[object, object, object, object, object, object]]] = FieldInfo(
        alias="runnerConfig", default=None
    )

    scm: Optional[List[SchemaScm]] = None

    version: Optional[str] = None
    """The schema version"""


class ConfigurationSchemaRetrieveResponse(BaseModel):
    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
