# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    secret_list_params,
    secret_create_params,
    secret_delete_params,
    secret_get_value_params,
    secret_update_value_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncSecretsPage, AsyncSecretsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.secret import Secret
from ..types.secret_create_response import SecretCreateResponse
from ..types.secret_get_value_response import SecretGetValueResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        environment_variable: bool | NotGiven = NOT_GIVEN,
        file_path: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretCreateResponse:
        """
        CreateSecret creates a new secret.

        Args:
          environment_variable: secret will be created as an Environment Variable with the same name as the
              secret

          file_path: absolute path to the file where the secret is mounted value must be an absolute
              path (start with a /):

              ```
              this.matches("^/(?:[^/]*/)*.*$")
              ```

          project_id: project_id is the ProjectID this Secret belongs to

          value: value is the plaintext value of the secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecretService/CreateSecret",
            body=maybe_transform(
                {
                    "environment_variable": environment_variable,
                    "file_path": file_path,
                    "name": name,
                    "project_id": project_id,
                    "value": value,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretCreateResponse,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: secret_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: secret_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSecretsPage[Secret]:
        """
        ListSecrets lists secrets.

        Args:
          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.SecretService/ListSecrets",
            page=SyncSecretsPage[Secret],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                secret_list_params.SecretListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            model=Secret,
            method="post",
        )

    def delete(
        self,
        *,
        secret_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteSecret deletes a secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecretService/DeleteSecret",
            body=maybe_transform({"secret_id": secret_id}, secret_delete_params.SecretDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_value(
        self,
        *,
        secret_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetValueResponse:
        """
        GetSecretValue retrieves the value of a secret Only Environments can perform
        this operation, and only for secrets specified on the EnvironmentSpec.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecretService/GetSecretValue",
            body=maybe_transform({"secret_id": secret_id}, secret_get_value_params.SecretGetValueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretGetValueResponse,
        )

    def update_value(
        self,
        *,
        secret_id: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSecretValue updates the value of a secret.

        Args:
          value: value is the plaintext value of the secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecretService/UpdateSecretValue",
            body=maybe_transform(
                {
                    "secret_id": secret_id,
                    "value": value,
                },
                secret_update_value_params.SecretUpdateValueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        environment_variable: bool | NotGiven = NOT_GIVEN,
        file_path: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretCreateResponse:
        """
        CreateSecret creates a new secret.

        Args:
          environment_variable: secret will be created as an Environment Variable with the same name as the
              secret

          file_path: absolute path to the file where the secret is mounted value must be an absolute
              path (start with a /):

              ```
              this.matches("^/(?:[^/]*/)*.*$")
              ```

          project_id: project_id is the ProjectID this Secret belongs to

          value: value is the plaintext value of the secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecretService/CreateSecret",
            body=await async_maybe_transform(
                {
                    "environment_variable": environment_variable,
                    "file_path": file_path,
                    "name": name,
                    "project_id": project_id,
                    "value": value,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretCreateResponse,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: secret_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: secret_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Secret, AsyncSecretsPage[Secret]]:
        """
        ListSecrets lists secrets.

        Args:
          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.SecretService/ListSecrets",
            page=AsyncSecretsPage[Secret],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                secret_list_params.SecretListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            model=Secret,
            method="post",
        )

    async def delete(
        self,
        *,
        secret_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteSecret deletes a secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecretService/DeleteSecret",
            body=await async_maybe_transform({"secret_id": secret_id}, secret_delete_params.SecretDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_value(
        self,
        *,
        secret_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetValueResponse:
        """
        GetSecretValue retrieves the value of a secret Only Environments can perform
        this operation, and only for secrets specified on the EnvironmentSpec.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecretService/GetSecretValue",
            body=await async_maybe_transform({"secret_id": secret_id}, secret_get_value_params.SecretGetValueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretGetValueResponse,
        )

    async def update_value(
        self,
        *,
        secret_id: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSecretValue updates the value of a secret.

        Args:
          value: value is the plaintext value of the secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecretService/UpdateSecretValue",
            body=await async_maybe_transform(
                {
                    "secret_id": secret_id,
                    "value": value,
                },
                secret_update_value_params.SecretUpdateValueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.get_value = to_raw_response_wrapper(
            secrets.get_value,
        )
        self.update_value = to_raw_response_wrapper(
            secrets.update_value,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.get_value = async_to_raw_response_wrapper(
            secrets.get_value,
        )
        self.update_value = async_to_raw_response_wrapper(
            secrets.update_value,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get_value = to_streamed_response_wrapper(
            secrets.get_value,
        )
        self.update_value = to_streamed_response_wrapper(
            secrets.update_value,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get_value = async_to_streamed_response_wrapper(
            secrets.get_value,
        )
        self.update_value = async_to_streamed_response_wrapper(
            secrets.update_value,
        )
