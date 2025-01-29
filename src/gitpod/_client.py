# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    tasks,
    editors,
    projects,
    services,
    environments,
    automations_files,
    environment_classes,
    personal_access_tokens,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.runners import runners
from .resources.organizations import organizations
from .resources.runner_interactions import runner_interactions
from .resources.runner_configurations import runner_configurations
from .resources.environment_automations import environment_automations

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Gitpod", "AsyncGitpod", "Client", "AsyncClient"]


class Gitpod(SyncAPIClient):
    services: services.ServicesResource
    automations_files: automations_files.AutomationsFilesResource
    tasks: tasks.TasksResource
    editors: editors.EditorsResource
    environment_automations: environment_automations.EnvironmentAutomationsResource
    environments: environments.EnvironmentsResource
    environment_classes: environment_classes.EnvironmentClassesResource
    organizations: organizations.OrganizationsResource
    projects: projects.ProjectsResource
    runner_configurations: runner_configurations.RunnerConfigurationsResource
    runner_interactions: runner_interactions.RunnerInteractionsResource
    runners: runners.RunnersResource
    personal_access_tokens: personal_access_tokens.PersonalAccessTokensResource
    with_raw_response: GitpodWithRawResponse
    with_streaming_response: GitpodWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new synchronous gitpod client instance."""
        if base_url is None:
            base_url = os.environ.get("GITPOD_BASE_URL")
        if base_url is None:
            base_url = f"https://localhost:8080/test-api"

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

        self.services = services.ServicesResource(self)
        self.automations_files = automations_files.AutomationsFilesResource(self)
        self.tasks = tasks.TasksResource(self)
        self.editors = editors.EditorsResource(self)
        self.environment_automations = environment_automations.EnvironmentAutomationsResource(self)
        self.environments = environments.EnvironmentsResource(self)
        self.environment_classes = environment_classes.EnvironmentClassesResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.projects = projects.ProjectsResource(self)
        self.runner_configurations = runner_configurations.RunnerConfigurationsResource(self)
        self.runner_interactions = runner_interactions.RunnerInteractionsResource(self)
        self.runners = runners.RunnersResource(self)
        self.personal_access_tokens = personal_access_tokens.PersonalAccessTokensResource(self)
        self.with_raw_response = GitpodWithRawResponse(self)
        self.with_streaming_response = GitpodWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    services: services.AsyncServicesResource
    automations_files: automations_files.AsyncAutomationsFilesResource
    tasks: tasks.AsyncTasksResource
    editors: editors.AsyncEditorsResource
    environment_automations: environment_automations.AsyncEnvironmentAutomationsResource
    environments: environments.AsyncEnvironmentsResource
    environment_classes: environment_classes.AsyncEnvironmentClassesResource
    organizations: organizations.AsyncOrganizationsResource
    projects: projects.AsyncProjectsResource
    runner_configurations: runner_configurations.AsyncRunnerConfigurationsResource
    runner_interactions: runner_interactions.AsyncRunnerInteractionsResource
    runners: runners.AsyncRunnersResource
    personal_access_tokens: personal_access_tokens.AsyncPersonalAccessTokensResource
    with_raw_response: AsyncGitpodWithRawResponse
    with_streaming_response: AsyncGitpodWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new async gitpod client instance."""
        if base_url is None:
            base_url = os.environ.get("GITPOD_BASE_URL")
        if base_url is None:
            base_url = f"https://localhost:8080/test-api"

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

        self.services = services.AsyncServicesResource(self)
        self.automations_files = automations_files.AsyncAutomationsFilesResource(self)
        self.tasks = tasks.AsyncTasksResource(self)
        self.editors = editors.AsyncEditorsResource(self)
        self.environment_automations = environment_automations.AsyncEnvironmentAutomationsResource(self)
        self.environments = environments.AsyncEnvironmentsResource(self)
        self.environment_classes = environment_classes.AsyncEnvironmentClassesResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.runner_configurations = runner_configurations.AsyncRunnerConfigurationsResource(self)
        self.runner_interactions = runner_interactions.AsyncRunnerInteractionsResource(self)
        self.runners = runners.AsyncRunnersResource(self)
        self.personal_access_tokens = personal_access_tokens.AsyncPersonalAccessTokensResource(self)
        self.with_raw_response = AsyncGitpodWithRawResponse(self)
        self.with_streaming_response = AsyncGitpodWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

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
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
        self.services = services.ServicesResourceWithRawResponse(client.services)
        self.automations_files = automations_files.AutomationsFilesResourceWithRawResponse(client.automations_files)
        self.tasks = tasks.TasksResourceWithRawResponse(client.tasks)
        self.editors = editors.EditorsResourceWithRawResponse(client.editors)
        self.environment_automations = environment_automations.EnvironmentAutomationsResourceWithRawResponse(
            client.environment_automations
        )
        self.environments = environments.EnvironmentsResourceWithRawResponse(client.environments)
        self.environment_classes = environment_classes.EnvironmentClassesResourceWithRawResponse(
            client.environment_classes
        )
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.runner_configurations = runner_configurations.RunnerConfigurationsResourceWithRawResponse(
            client.runner_configurations
        )
        self.runner_interactions = runner_interactions.RunnerInteractionsResourceWithRawResponse(
            client.runner_interactions
        )
        self.runners = runners.RunnersResourceWithRawResponse(client.runners)
        self.personal_access_tokens = personal_access_tokens.PersonalAccessTokensResourceWithRawResponse(
            client.personal_access_tokens
        )


class AsyncGitpodWithRawResponse:
    def __init__(self, client: AsyncGitpod) -> None:
        self.services = services.AsyncServicesResourceWithRawResponse(client.services)
        self.automations_files = automations_files.AsyncAutomationsFilesResourceWithRawResponse(
            client.automations_files
        )
        self.tasks = tasks.AsyncTasksResourceWithRawResponse(client.tasks)
        self.editors = editors.AsyncEditorsResourceWithRawResponse(client.editors)
        self.environment_automations = environment_automations.AsyncEnvironmentAutomationsResourceWithRawResponse(
            client.environment_automations
        )
        self.environments = environments.AsyncEnvironmentsResourceWithRawResponse(client.environments)
        self.environment_classes = environment_classes.AsyncEnvironmentClassesResourceWithRawResponse(
            client.environment_classes
        )
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.runner_configurations = runner_configurations.AsyncRunnerConfigurationsResourceWithRawResponse(
            client.runner_configurations
        )
        self.runner_interactions = runner_interactions.AsyncRunnerInteractionsResourceWithRawResponse(
            client.runner_interactions
        )
        self.runners = runners.AsyncRunnersResourceWithRawResponse(client.runners)
        self.personal_access_tokens = personal_access_tokens.AsyncPersonalAccessTokensResourceWithRawResponse(
            client.personal_access_tokens
        )


class GitpodWithStreamedResponse:
    def __init__(self, client: Gitpod) -> None:
        self.services = services.ServicesResourceWithStreamingResponse(client.services)
        self.automations_files = automations_files.AutomationsFilesResourceWithStreamingResponse(
            client.automations_files
        )
        self.tasks = tasks.TasksResourceWithStreamingResponse(client.tasks)
        self.editors = editors.EditorsResourceWithStreamingResponse(client.editors)
        self.environment_automations = environment_automations.EnvironmentAutomationsResourceWithStreamingResponse(
            client.environment_automations
        )
        self.environments = environments.EnvironmentsResourceWithStreamingResponse(client.environments)
        self.environment_classes = environment_classes.EnvironmentClassesResourceWithStreamingResponse(
            client.environment_classes
        )
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.runner_configurations = runner_configurations.RunnerConfigurationsResourceWithStreamingResponse(
            client.runner_configurations
        )
        self.runner_interactions = runner_interactions.RunnerInteractionsResourceWithStreamingResponse(
            client.runner_interactions
        )
        self.runners = runners.RunnersResourceWithStreamingResponse(client.runners)
        self.personal_access_tokens = personal_access_tokens.PersonalAccessTokensResourceWithStreamingResponse(
            client.personal_access_tokens
        )


class AsyncGitpodWithStreamedResponse:
    def __init__(self, client: AsyncGitpod) -> None:
        self.services = services.AsyncServicesResourceWithStreamingResponse(client.services)
        self.automations_files = automations_files.AsyncAutomationsFilesResourceWithStreamingResponse(
            client.automations_files
        )
        self.tasks = tasks.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.editors = editors.AsyncEditorsResourceWithStreamingResponse(client.editors)
        self.environment_automations = environment_automations.AsyncEnvironmentAutomationsResourceWithStreamingResponse(
            client.environment_automations
        )
        self.environments = environments.AsyncEnvironmentsResourceWithStreamingResponse(client.environments)
        self.environment_classes = environment_classes.AsyncEnvironmentClassesResourceWithStreamingResponse(
            client.environment_classes
        )
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.runner_configurations = runner_configurations.AsyncRunnerConfigurationsResourceWithStreamingResponse(
            client.runner_configurations
        )
        self.runner_interactions = runner_interactions.AsyncRunnerInteractionsResourceWithStreamingResponse(
            client.runner_interactions
        )
        self.runners = runners.AsyncRunnersResourceWithStreamingResponse(client.runners)
        self.personal_access_tokens = personal_access_tokens.AsyncPersonalAccessTokensResourceWithStreamingResponse(
            client.personal_access_tokens
        )


Client = Gitpod

AsyncClient = AsyncGitpod
