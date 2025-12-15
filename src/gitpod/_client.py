# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import usage, agents, errors, events, editors, secrets, accounts, gateways, identity, prebuilds
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import GitpodError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.users import users
from .resources.groups import groups
from .resources.runners import runners
from .resources.projects import projects
from .resources.environments import environments
from .resources.organizations import organizations

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Gitpod", "AsyncGitpod", "Client", "AsyncClient"]


class Gitpod(SyncAPIClient):
    accounts: accounts.AccountsResource
    agents: agents.AgentsResource
    editors: editors.EditorsResource
    environments: environments.EnvironmentsResource
    errors: errors.ErrorsResource
    events: events.EventsResource
    gateways: gateways.GatewaysResource
    groups: groups.GroupsResource
    identity: identity.IdentityResource
    organizations: organizations.OrganizationsResource
    prebuilds: prebuilds.PrebuildsResource
    projects: projects.ProjectsResource
    runners: runners.RunnersResource
    secrets: secrets.SecretsResource
    usage: usage.UsageResource
    users: users.UsersResource
    with_raw_response: GitpodWithRawResponse
    with_streaming_response: GitpodWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Gitpod client instance.

        This automatically infers the `bearer_token` argument from the `GITPOD_API_KEY` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("GITPOD_API_KEY")
        if bearer_token is None:
            raise GitpodError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the GITPOD_API_KEY environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("GITPOD_BASE_URL")
        if base_url is None:
            base_url = f"https://app.gitpod.io/api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AccountsResource(self)
        self.agents = agents.AgentsResource(self)
        self.editors = editors.EditorsResource(self)
        self.environments = environments.EnvironmentsResource(self)
        self.errors = errors.ErrorsResource(self)
        self.events = events.EventsResource(self)
        self.gateways = gateways.GatewaysResource(self)
        self.groups = groups.GroupsResource(self)
        self.identity = identity.IdentityResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.prebuilds = prebuilds.PrebuildsResource(self)
        self.projects = projects.ProjectsResource(self)
        self.runners = runners.RunnersResource(self)
        self.secrets = secrets.SecretsResource(self)
        self.usage = usage.UsageResource(self)
        self.users = users.UsersResource(self)
        self.with_raw_response = GitpodWithRawResponse(self)
        self.with_streaming_response = GitpodWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGitpod(AsyncAPIClient):
    accounts: accounts.AsyncAccountsResource
    agents: agents.AsyncAgentsResource
    editors: editors.AsyncEditorsResource
    environments: environments.AsyncEnvironmentsResource
    errors: errors.AsyncErrorsResource
    events: events.AsyncEventsResource
    gateways: gateways.AsyncGatewaysResource
    groups: groups.AsyncGroupsResource
    identity: identity.AsyncIdentityResource
    organizations: organizations.AsyncOrganizationsResource
    prebuilds: prebuilds.AsyncPrebuildsResource
    projects: projects.AsyncProjectsResource
    runners: runners.AsyncRunnersResource
    secrets: secrets.AsyncSecretsResource
    usage: usage.AsyncUsageResource
    users: users.AsyncUsersResource
    with_raw_response: AsyncGitpodWithRawResponse
    with_streaming_response: AsyncGitpodWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGitpod client instance.

        This automatically infers the `bearer_token` argument from the `GITPOD_API_KEY` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("GITPOD_API_KEY")
        if bearer_token is None:
            raise GitpodError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the GITPOD_API_KEY environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("GITPOD_BASE_URL")
        if base_url is None:
            base_url = f"https://app.gitpod.io/api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AsyncAccountsResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.editors = editors.AsyncEditorsResource(self)
        self.environments = environments.AsyncEnvironmentsResource(self)
        self.errors = errors.AsyncErrorsResource(self)
        self.events = events.AsyncEventsResource(self)
        self.gateways = gateways.AsyncGatewaysResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.identity = identity.AsyncIdentityResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.prebuilds = prebuilds.AsyncPrebuildsResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.runners = runners.AsyncRunnersResource(self)
        self.secrets = secrets.AsyncSecretsResource(self)
        self.usage = usage.AsyncUsageResource(self)
        self.users = users.AsyncUsersResource(self)
        self.with_raw_response = AsyncGitpodWithRawResponse(self)
        self.with_streaming_response = AsyncGitpodWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GitpodWithRawResponse:
    def __init__(self, client: Gitpod) -> None:
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.editors = editors.EditorsResourceWithRawResponse(client.editors)
        self.environments = environments.EnvironmentsResourceWithRawResponse(client.environments)
        self.errors = errors.ErrorsResourceWithRawResponse(client.errors)
        self.events = events.EventsResourceWithRawResponse(client.events)
        self.gateways = gateways.GatewaysResourceWithRawResponse(client.gateways)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.identity = identity.IdentityResourceWithRawResponse(client.identity)
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.prebuilds = prebuilds.PrebuildsResourceWithRawResponse(client.prebuilds)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.runners = runners.RunnersResourceWithRawResponse(client.runners)
        self.secrets = secrets.SecretsResourceWithRawResponse(client.secrets)
        self.usage = usage.UsageResourceWithRawResponse(client.usage)
        self.users = users.UsersResourceWithRawResponse(client.users)


class AsyncGitpodWithRawResponse:
    def __init__(self, client: AsyncGitpod) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.editors = editors.AsyncEditorsResourceWithRawResponse(client.editors)
        self.environments = environments.AsyncEnvironmentsResourceWithRawResponse(client.environments)
        self.errors = errors.AsyncErrorsResourceWithRawResponse(client.errors)
        self.events = events.AsyncEventsResourceWithRawResponse(client.events)
        self.gateways = gateways.AsyncGatewaysResourceWithRawResponse(client.gateways)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.identity = identity.AsyncIdentityResourceWithRawResponse(client.identity)
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.prebuilds = prebuilds.AsyncPrebuildsResourceWithRawResponse(client.prebuilds)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.runners = runners.AsyncRunnersResourceWithRawResponse(client.runners)
        self.secrets = secrets.AsyncSecretsResourceWithRawResponse(client.secrets)
        self.usage = usage.AsyncUsageResourceWithRawResponse(client.usage)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)


class GitpodWithStreamedResponse:
    def __init__(self, client: Gitpod) -> None:
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.editors = editors.EditorsResourceWithStreamingResponse(client.editors)
        self.environments = environments.EnvironmentsResourceWithStreamingResponse(client.environments)
        self.errors = errors.ErrorsResourceWithStreamingResponse(client.errors)
        self.events = events.EventsResourceWithStreamingResponse(client.events)
        self.gateways = gateways.GatewaysResourceWithStreamingResponse(client.gateways)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.identity = identity.IdentityResourceWithStreamingResponse(client.identity)
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.prebuilds = prebuilds.PrebuildsResourceWithStreamingResponse(client.prebuilds)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.runners = runners.RunnersResourceWithStreamingResponse(client.runners)
        self.secrets = secrets.SecretsResourceWithStreamingResponse(client.secrets)
        self.usage = usage.UsageResourceWithStreamingResponse(client.usage)
        self.users = users.UsersResourceWithStreamingResponse(client.users)


class AsyncGitpodWithStreamedResponse:
    def __init__(self, client: AsyncGitpod) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.editors = editors.AsyncEditorsResourceWithStreamingResponse(client.editors)
        self.environments = environments.AsyncEnvironmentsResourceWithStreamingResponse(client.environments)
        self.errors = errors.AsyncErrorsResourceWithStreamingResponse(client.errors)
        self.events = events.AsyncEventsResourceWithStreamingResponse(client.events)
        self.gateways = gateways.AsyncGatewaysResourceWithStreamingResponse(client.gateways)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.identity = identity.AsyncIdentityResourceWithStreamingResponse(client.identity)
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.prebuilds = prebuilds.AsyncPrebuildsResourceWithStreamingResponse(client.prebuilds)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.runners = runners.AsyncRunnersResourceWithStreamingResponse(client.runners)
        self.secrets = secrets.AsyncSecretsResourceWithStreamingResponse(client.secrets)
        self.usage = usage.AsyncUsageResourceWithStreamingResponse(client.usage)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)


Client = Gitpod

AsyncClient = AsyncGitpod
