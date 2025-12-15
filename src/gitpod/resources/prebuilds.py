# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    prebuild_list_params,
    prebuild_cancel_params,
    prebuild_create_params,
    prebuild_delete_params,
    prebuild_retrieve_params,
    prebuild_create_logs_token_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPrebuildsPage, AsyncPrebuildsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.prebuild import Prebuild
from ..types.prebuild_spec_param import PrebuildSpecParam
from ..types.prebuild_cancel_response import PrebuildCancelResponse
from ..types.prebuild_create_response import PrebuildCreateResponse
from ..types.prebuild_retrieve_response import PrebuildRetrieveResponse
from ..types.prebuild_create_logs_token_response import PrebuildCreateLogsTokenResponse

__all__ = ["PrebuildsResource", "AsyncPrebuildsResource"]


class PrebuildsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrebuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PrebuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrebuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return PrebuildsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        spec: PrebuildSpecParam,
        environment_class_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildCreateResponse:
        """
        Creates a prebuild for a project.

        Use this method to:

        - Create on-demand prebuilds for faster environment startup
        - Trigger prebuilds after repository changes
        - Generate prebuilds for specific environment classes

        The prebuild process creates an environment, runs the devcontainer prebuild
        lifecycle, and creates a snapshot for future environment provisioning.

        ### Examples

        - Create basic prebuild:

          Creates a prebuild for a project using default settings.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          spec:
            timeout: "3600s" # 60 minutes default
          ```

        - Create prebuild with custom environment class:

          Creates a prebuild with a specific environment class and timeout.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          environmentClassId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            timeout: "3600s" # 1 hour
          ```

        Args:
          project_id: project_id specifies the project to create a prebuild for

          spec: spec contains the configuration for creating the prebuild

          environment_class_id: environment_class_id specifies which environment class to use for the prebuild.
              If not specified, uses the project's default environment class.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.PrebuildService/CreatePrebuild",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "spec": spec,
                    "environment_class_id": environment_class_id,
                },
                prebuild_create_params.PrebuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildCreateResponse,
        )

    def retrieve(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildRetrieveResponse:
        """
        Gets details about a specific prebuild.

        Use this method to:

        - Check prebuild status and progress
        - Access prebuild logs for debugging

        ### Examples

        - Get prebuild details:

          Retrieves comprehensive information about a prebuild.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.PrebuildService/GetPrebuild",
            body=maybe_transform({"prebuild_id": prebuild_id}, prebuild_retrieve_params.PrebuildRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildRetrieveResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: prebuild_list_params.Filter | Omit = omit,
        pagination: prebuild_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPrebuildsPage[Prebuild]:
        """
        ListPrebuilds

        Args:
          filter: filter contains the filter options for listing prebuilds

          pagination: pagination contains the pagination options for listing prebuilds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.PrebuildService/ListPrebuilds",
            page=SyncPrebuildsPage[Prebuild],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                prebuild_list_params.PrebuildListParams,
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
                    prebuild_list_params.PrebuildListParams,
                ),
            ),
            model=Prebuild,
            method="post",
        )

    def delete(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Deletes a prebuild.

        Prebuilds are automatically deleted after some time.

        Use this method to manually
        delete a prebuild before automatic cleanup, for example to remove a prebuild
        that should no longer be used.

        Deletion is processed asynchronously. The prebuild will be marked for deletion
        and removed from the system in the background.

        ### Examples

        - Delete prebuild:

          Marks a prebuild for deletion and removes it from the system.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.PrebuildService/DeletePrebuild",
            body=maybe_transform({"prebuild_id": prebuild_id}, prebuild_delete_params.PrebuildDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def cancel(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildCancelResponse:
        """
        Cancels a running prebuild.

        Use this method to:

        - Stop prebuilds that are no longer needed
        - Free up resources for other operations

        ### Examples

        - Cancel prebuild:

          Stops a running prebuild and cleans up resources.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.PrebuildService/CancelPrebuild",
            body=maybe_transform({"prebuild_id": prebuild_id}, prebuild_cancel_params.PrebuildCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildCancelResponse,
        )

    def create_logs_token(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildCreateLogsTokenResponse:
        """
        Creates a logs access token for a prebuild.

        Use this method to:

        - Stream logs from a running prebuild
        - Access archived logs from completed prebuilds

        Generated tokens are valid for one hour.

        ### Examples

        - Create prebuild logs token:

          Generates a token for accessing prebuild logs.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild for which the logs token should be created.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.PrebuildService/CreatePrebuildLogsToken",
            body=maybe_transform(
                {"prebuild_id": prebuild_id}, prebuild_create_logs_token_params.PrebuildCreateLogsTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildCreateLogsTokenResponse,
        )


class AsyncPrebuildsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrebuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrebuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrebuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncPrebuildsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        spec: PrebuildSpecParam,
        environment_class_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildCreateResponse:
        """
        Creates a prebuild for a project.

        Use this method to:

        - Create on-demand prebuilds for faster environment startup
        - Trigger prebuilds after repository changes
        - Generate prebuilds for specific environment classes

        The prebuild process creates an environment, runs the devcontainer prebuild
        lifecycle, and creates a snapshot for future environment provisioning.

        ### Examples

        - Create basic prebuild:

          Creates a prebuild for a project using default settings.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          spec:
            timeout: "3600s" # 60 minutes default
          ```

        - Create prebuild with custom environment class:

          Creates a prebuild with a specific environment class and timeout.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          environmentClassId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            timeout: "3600s" # 1 hour
          ```

        Args:
          project_id: project_id specifies the project to create a prebuild for

          spec: spec contains the configuration for creating the prebuild

          environment_class_id: environment_class_id specifies which environment class to use for the prebuild.
              If not specified, uses the project's default environment class.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.PrebuildService/CreatePrebuild",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "spec": spec,
                    "environment_class_id": environment_class_id,
                },
                prebuild_create_params.PrebuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildCreateResponse,
        )

    async def retrieve(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildRetrieveResponse:
        """
        Gets details about a specific prebuild.

        Use this method to:

        - Check prebuild status and progress
        - Access prebuild logs for debugging

        ### Examples

        - Get prebuild details:

          Retrieves comprehensive information about a prebuild.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.PrebuildService/GetPrebuild",
            body=await async_maybe_transform(
                {"prebuild_id": prebuild_id}, prebuild_retrieve_params.PrebuildRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildRetrieveResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: prebuild_list_params.Filter | Omit = omit,
        pagination: prebuild_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Prebuild, AsyncPrebuildsPage[Prebuild]]:
        """
        ListPrebuilds

        Args:
          filter: filter contains the filter options for listing prebuilds

          pagination: pagination contains the pagination options for listing prebuilds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.PrebuildService/ListPrebuilds",
            page=AsyncPrebuildsPage[Prebuild],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                prebuild_list_params.PrebuildListParams,
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
                    prebuild_list_params.PrebuildListParams,
                ),
            ),
            model=Prebuild,
            method="post",
        )

    async def delete(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Deletes a prebuild.

        Prebuilds are automatically deleted after some time.

        Use this method to manually
        delete a prebuild before automatic cleanup, for example to remove a prebuild
        that should no longer be used.

        Deletion is processed asynchronously. The prebuild will be marked for deletion
        and removed from the system in the background.

        ### Examples

        - Delete prebuild:

          Marks a prebuild for deletion and removes it from the system.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.PrebuildService/DeletePrebuild",
            body=await async_maybe_transform({"prebuild_id": prebuild_id}, prebuild_delete_params.PrebuildDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def cancel(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildCancelResponse:
        """
        Cancels a running prebuild.

        Use this method to:

        - Stop prebuilds that are no longer needed
        - Free up resources for other operations

        ### Examples

        - Cancel prebuild:

          Stops a running prebuild and cleans up resources.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.PrebuildService/CancelPrebuild",
            body=await async_maybe_transform({"prebuild_id": prebuild_id}, prebuild_cancel_params.PrebuildCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildCancelResponse,
        )

    async def create_logs_token(
        self,
        *,
        prebuild_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrebuildCreateLogsTokenResponse:
        """
        Creates a logs access token for a prebuild.

        Use this method to:

        - Stream logs from a running prebuild
        - Access archived logs from completed prebuilds

        Generated tokens are valid for one hour.

        ### Examples

        - Create prebuild logs token:

          Generates a token for accessing prebuild logs.

          ```yaml
          prebuildId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          prebuild_id: prebuild_id specifies the prebuild for which the logs token should be created.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.PrebuildService/CreatePrebuildLogsToken",
            body=await async_maybe_transform(
                {"prebuild_id": prebuild_id}, prebuild_create_logs_token_params.PrebuildCreateLogsTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrebuildCreateLogsTokenResponse,
        )


class PrebuildsResourceWithRawResponse:
    def __init__(self, prebuilds: PrebuildsResource) -> None:
        self._prebuilds = prebuilds

        self.create = to_raw_response_wrapper(
            prebuilds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prebuilds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            prebuilds.list,
        )
        self.delete = to_raw_response_wrapper(
            prebuilds.delete,
        )
        self.cancel = to_raw_response_wrapper(
            prebuilds.cancel,
        )
        self.create_logs_token = to_raw_response_wrapper(
            prebuilds.create_logs_token,
        )


class AsyncPrebuildsResourceWithRawResponse:
    def __init__(self, prebuilds: AsyncPrebuildsResource) -> None:
        self._prebuilds = prebuilds

        self.create = async_to_raw_response_wrapper(
            prebuilds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prebuilds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            prebuilds.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prebuilds.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            prebuilds.cancel,
        )
        self.create_logs_token = async_to_raw_response_wrapper(
            prebuilds.create_logs_token,
        )


class PrebuildsResourceWithStreamingResponse:
    def __init__(self, prebuilds: PrebuildsResource) -> None:
        self._prebuilds = prebuilds

        self.create = to_streamed_response_wrapper(
            prebuilds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prebuilds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            prebuilds.list,
        )
        self.delete = to_streamed_response_wrapper(
            prebuilds.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            prebuilds.cancel,
        )
        self.create_logs_token = to_streamed_response_wrapper(
            prebuilds.create_logs_token,
        )


class AsyncPrebuildsResourceWithStreamingResponse:
    def __init__(self, prebuilds: AsyncPrebuildsResource) -> None:
        self._prebuilds = prebuilds

        self.create = async_to_streamed_response_wrapper(
            prebuilds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prebuilds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            prebuilds.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prebuilds.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            prebuilds.cancel,
        )
        self.create_logs_token = async_to_streamed_response_wrapper(
            prebuilds.create_logs_token,
        )
