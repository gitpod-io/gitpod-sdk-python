# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import GitpodError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        usage,
        users,
        agents,
        errors,
        events,
        groups,
        editors,
        runners,
        secrets,
        accounts,
        gateways,
        identity,
        projects,
        prebuilds,
        environments,
        organizations,
    )
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.agents import AgentsResource, AsyncAgentsResource
    from .resources.errors import ErrorsResource, AsyncErrorsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.editors import EditorsResource, AsyncEditorsResource
    from .resources.secrets import SecretsResource, AsyncSecretsResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.gateways import GatewaysResource, AsyncGatewaysResource
    from .resources.identity import IdentityResource, AsyncIdentityResource
    from .resources.prebuilds import PrebuildsResource, AsyncPrebuildsResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.groups.groups import GroupsResource, AsyncGroupsResource
    from .resources.runners.runners import RunnersResource, AsyncRunnersResource
    from .resources.projects.projects import ProjectsResource, AsyncProjectsResource
    from .resources.environments.environments import EnvironmentsResource, AsyncEnvironmentsResource
    from .resources.organizations.organizations import OrganizationsResource, AsyncOrganizationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Gitpod", "AsyncGitpod", "Client", "AsyncClient"]


class Gitpod(SyncAPIClient):
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

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def editors(self) -> EditorsResource:
        from .resources.editors import EditorsResource

        return EditorsResource(self)

    @cached_property
    def environments(self) -> EnvironmentsResource:
        from .resources.environments import EnvironmentsResource

        return EnvironmentsResource(self)

    @cached_property
    def errors(self) -> ErrorsResource:
        from .resources.errors import ErrorsResource

        return ErrorsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def gateways(self) -> GatewaysResource:
        from .resources.gateways import GatewaysResource

        return GatewaysResource(self)

    @cached_property
    def groups(self) -> GroupsResource:
        from .resources.groups import GroupsResource

        return GroupsResource(self)

    @cached_property
    def identity(self) -> IdentityResource:
        from .resources.identity import IdentityResource

        return IdentityResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def prebuilds(self) -> PrebuildsResource:
        from .resources.prebuilds import PrebuildsResource

        return PrebuildsResource(self)

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def runners(self) -> RunnersResource:
        from .resources.runners import RunnersResource

        return RunnersResource(self)

    @cached_property
    def secrets(self) -> SecretsResource:
        from .resources.secrets import SecretsResource

        return SecretsResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def with_raw_response(self) -> GitpodWithRawResponse:
        return GitpodWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitpodWithStreamedResponse:
        return GitpodWithStreamedResponse(self)

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

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def editors(self) -> AsyncEditorsResource:
        from .resources.editors import AsyncEditorsResource

        return AsyncEditorsResource(self)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResource:
        from .resources.environments import AsyncEnvironmentsResource

        return AsyncEnvironmentsResource(self)

    @cached_property
    def errors(self) -> AsyncErrorsResource:
        from .resources.errors import AsyncErrorsResource

        return AsyncErrorsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def gateways(self) -> AsyncGatewaysResource:
        from .resources.gateways import AsyncGatewaysResource

        return AsyncGatewaysResource(self)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        from .resources.groups import AsyncGroupsResource

        return AsyncGroupsResource(self)

    @cached_property
    def identity(self) -> AsyncIdentityResource:
        from .resources.identity import AsyncIdentityResource

        return AsyncIdentityResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def prebuilds(self) -> AsyncPrebuildsResource:
        from .resources.prebuilds import AsyncPrebuildsResource

        return AsyncPrebuildsResource(self)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def runners(self) -> AsyncRunnersResource:
        from .resources.runners import AsyncRunnersResource

        return AsyncRunnersResource(self)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        from .resources.secrets import AsyncSecretsResource

        return AsyncSecretsResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGitpodWithRawResponse:
        return AsyncGitpodWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitpodWithStreamedResponse:
        return AsyncGitpodWithStreamedResponse(self)

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
    _client: Gitpod

    def __init__(self, client: Gitpod) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def editors(self) -> editors.EditorsResourceWithRawResponse:
        from .resources.editors import EditorsResourceWithRawResponse

        return EditorsResourceWithRawResponse(self._client.editors)

    @cached_property
    def environments(self) -> environments.EnvironmentsResourceWithRawResponse:
        from .resources.environments import EnvironmentsResourceWithRawResponse

        return EnvironmentsResourceWithRawResponse(self._client.environments)

    @cached_property
    def errors(self) -> errors.ErrorsResourceWithRawResponse:
        from .resources.errors import ErrorsResourceWithRawResponse

        return ErrorsResourceWithRawResponse(self._client.errors)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def gateways(self) -> gateways.GatewaysResourceWithRawResponse:
        from .resources.gateways import GatewaysResourceWithRawResponse

        return GatewaysResourceWithRawResponse(self._client.gateways)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithRawResponse:
        from .resources.groups import GroupsResourceWithRawResponse

        return GroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def identity(self) -> identity.IdentityResourceWithRawResponse:
        from .resources.identity import IdentityResourceWithRawResponse

        return IdentityResourceWithRawResponse(self._client.identity)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prebuilds(self) -> prebuilds.PrebuildsResourceWithRawResponse:
        from .resources.prebuilds import PrebuildsResourceWithRawResponse

        return PrebuildsResourceWithRawResponse(self._client.prebuilds)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def runners(self) -> runners.RunnersResourceWithRawResponse:
        from .resources.runners import RunnersResourceWithRawResponse

        return RunnersResourceWithRawResponse(self._client.runners)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithRawResponse:
        from .resources.secrets import SecretsResourceWithRawResponse

        return SecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)


class AsyncGitpodWithRawResponse:
    _client: AsyncGitpod

    def __init__(self, client: AsyncGitpod) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def editors(self) -> editors.AsyncEditorsResourceWithRawResponse:
        from .resources.editors import AsyncEditorsResourceWithRawResponse

        return AsyncEditorsResourceWithRawResponse(self._client.editors)

    @cached_property
    def environments(self) -> environments.AsyncEnvironmentsResourceWithRawResponse:
        from .resources.environments import AsyncEnvironmentsResourceWithRawResponse

        return AsyncEnvironmentsResourceWithRawResponse(self._client.environments)

    @cached_property
    def errors(self) -> errors.AsyncErrorsResourceWithRawResponse:
        from .resources.errors import AsyncErrorsResourceWithRawResponse

        return AsyncErrorsResourceWithRawResponse(self._client.errors)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def gateways(self) -> gateways.AsyncGatewaysResourceWithRawResponse:
        from .resources.gateways import AsyncGatewaysResourceWithRawResponse

        return AsyncGatewaysResourceWithRawResponse(self._client.gateways)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithRawResponse:
        from .resources.groups import AsyncGroupsResourceWithRawResponse

        return AsyncGroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def identity(self) -> identity.AsyncIdentityResourceWithRawResponse:
        from .resources.identity import AsyncIdentityResourceWithRawResponse

        return AsyncIdentityResourceWithRawResponse(self._client.identity)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prebuilds(self) -> prebuilds.AsyncPrebuildsResourceWithRawResponse:
        from .resources.prebuilds import AsyncPrebuildsResourceWithRawResponse

        return AsyncPrebuildsResourceWithRawResponse(self._client.prebuilds)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def runners(self) -> runners.AsyncRunnersResourceWithRawResponse:
        from .resources.runners import AsyncRunnersResourceWithRawResponse

        return AsyncRunnersResourceWithRawResponse(self._client.runners)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithRawResponse:
        from .resources.secrets import AsyncSecretsResourceWithRawResponse

        return AsyncSecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)


class GitpodWithStreamedResponse:
    _client: Gitpod

    def __init__(self, client: Gitpod) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def editors(self) -> editors.EditorsResourceWithStreamingResponse:
        from .resources.editors import EditorsResourceWithStreamingResponse

        return EditorsResourceWithStreamingResponse(self._client.editors)

    @cached_property
    def environments(self) -> environments.EnvironmentsResourceWithStreamingResponse:
        from .resources.environments import EnvironmentsResourceWithStreamingResponse

        return EnvironmentsResourceWithStreamingResponse(self._client.environments)

    @cached_property
    def errors(self) -> errors.ErrorsResourceWithStreamingResponse:
        from .resources.errors import ErrorsResourceWithStreamingResponse

        return ErrorsResourceWithStreamingResponse(self._client.errors)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def gateways(self) -> gateways.GatewaysResourceWithStreamingResponse:
        from .resources.gateways import GatewaysResourceWithStreamingResponse

        return GatewaysResourceWithStreamingResponse(self._client.gateways)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithStreamingResponse:
        from .resources.groups import GroupsResourceWithStreamingResponse

        return GroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def identity(self) -> identity.IdentityResourceWithStreamingResponse:
        from .resources.identity import IdentityResourceWithStreamingResponse

        return IdentityResourceWithStreamingResponse(self._client.identity)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prebuilds(self) -> prebuilds.PrebuildsResourceWithStreamingResponse:
        from .resources.prebuilds import PrebuildsResourceWithStreamingResponse

        return PrebuildsResourceWithStreamingResponse(self._client.prebuilds)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def runners(self) -> runners.RunnersResourceWithStreamingResponse:
        from .resources.runners import RunnersResourceWithStreamingResponse

        return RunnersResourceWithStreamingResponse(self._client.runners)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithStreamingResponse:
        from .resources.secrets import SecretsResourceWithStreamingResponse

        return SecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)


class AsyncGitpodWithStreamedResponse:
    _client: AsyncGitpod

    def __init__(self, client: AsyncGitpod) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def editors(self) -> editors.AsyncEditorsResourceWithStreamingResponse:
        from .resources.editors import AsyncEditorsResourceWithStreamingResponse

        return AsyncEditorsResourceWithStreamingResponse(self._client.editors)

    @cached_property
    def environments(self) -> environments.AsyncEnvironmentsResourceWithStreamingResponse:
        from .resources.environments import AsyncEnvironmentsResourceWithStreamingResponse

        return AsyncEnvironmentsResourceWithStreamingResponse(self._client.environments)

    @cached_property
    def errors(self) -> errors.AsyncErrorsResourceWithStreamingResponse:
        from .resources.errors import AsyncErrorsResourceWithStreamingResponse

        return AsyncErrorsResourceWithStreamingResponse(self._client.errors)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def gateways(self) -> gateways.AsyncGatewaysResourceWithStreamingResponse:
        from .resources.gateways import AsyncGatewaysResourceWithStreamingResponse

        return AsyncGatewaysResourceWithStreamingResponse(self._client.gateways)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithStreamingResponse:
        from .resources.groups import AsyncGroupsResourceWithStreamingResponse

        return AsyncGroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def identity(self) -> identity.AsyncIdentityResourceWithStreamingResponse:
        from .resources.identity import AsyncIdentityResourceWithStreamingResponse

        return AsyncIdentityResourceWithStreamingResponse(self._client.identity)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prebuilds(self) -> prebuilds.AsyncPrebuildsResourceWithStreamingResponse:
        from .resources.prebuilds import AsyncPrebuildsResourceWithStreamingResponse

        return AsyncPrebuildsResourceWithStreamingResponse(self._client.prebuilds)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def runners(self) -> runners.AsyncRunnersResourceWithStreamingResponse:
        from .resources.runners import AsyncRunnersResourceWithStreamingResponse

        return AsyncRunnersResourceWithStreamingResponse(self._client.runners)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithStreamingResponse:
        from .resources.secrets import AsyncSecretsResourceWithStreamingResponse

        return AsyncSecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = Gitpod

AsyncClient = AsyncGitpod
