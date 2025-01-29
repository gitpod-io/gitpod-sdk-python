# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import editor_list_params, editor_retrieve_params, editor_resolve_editor_url_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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
from .._base_client import make_request_options
from ..types.editor_list_response import EditorListResponse
from ..types.editor_retrieve_response import EditorRetrieveResponse
from ..types.editor_resolve_editor_url_response import EditorResolveEditorURLResponse

__all__ = ["EditorsResource", "AsyncEditorsResource"]


class EditorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EditorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return EditorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EditorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return EditorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditorRetrieveResponse:
        """
        GetEditor returns the editor with the given ID

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          id: id is the ID of the editor to get

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/gitpod.v1.EditorService/GetEditor",
            body=maybe_transform({"id": id}, editor_retrieve_params.EditorRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditorRetrieveResponse,
        )

    def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        pagination: editor_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditorListResponse:
        """
        ListEditors lists all editors available to the caller

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing environments

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/gitpod.v1.EditorService/ListEditors",
            body=maybe_transform({"pagination": pagination}, editor_list_params.EditorListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditorListResponse,
        )

    def resolve_editor_url(
        self,
        *,
        connect_protocol_version: Literal[1],
        editor_id: str | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditorResolveEditorURLResponse:
        """
        ResolveEditorURL resolves the editor's URL for an environment

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          editor_id: editorId is the ID of the editor to resolve the URL for

          environment_id: environmentId is the ID of the environment to resolve the URL for

          organization_id: organizationId is the ID of the organization to resolve the URL for

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/gitpod.v1.EditorService/ResolveEditorURL",
            body=maybe_transform(
                {
                    "editor_id": editor_id,
                    "environment_id": environment_id,
                    "organization_id": organization_id,
                },
                editor_resolve_editor_url_params.EditorResolveEditorURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditorResolveEditorURLResponse,
        )


class AsyncEditorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEditorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEditorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEditorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncEditorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditorRetrieveResponse:
        """
        GetEditor returns the editor with the given ID

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          id: id is the ID of the editor to get

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/gitpod.v1.EditorService/GetEditor",
            body=await async_maybe_transform({"id": id}, editor_retrieve_params.EditorRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditorRetrieveResponse,
        )

    async def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        pagination: editor_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditorListResponse:
        """
        ListEditors lists all editors available to the caller

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing environments

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/gitpod.v1.EditorService/ListEditors",
            body=await async_maybe_transform({"pagination": pagination}, editor_list_params.EditorListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditorListResponse,
        )

    async def resolve_editor_url(
        self,
        *,
        connect_protocol_version: Literal[1],
        editor_id: str | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditorResolveEditorURLResponse:
        """
        ResolveEditorURL resolves the editor's URL for an environment

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          editor_id: editorId is the ID of the editor to resolve the URL for

          environment_id: environmentId is the ID of the environment to resolve the URL for

          organization_id: organizationId is the ID of the organization to resolve the URL for

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/gitpod.v1.EditorService/ResolveEditorURL",
            body=await async_maybe_transform(
                {
                    "editor_id": editor_id,
                    "environment_id": environment_id,
                    "organization_id": organization_id,
                },
                editor_resolve_editor_url_params.EditorResolveEditorURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditorResolveEditorURLResponse,
        )


class EditorsResourceWithRawResponse:
    def __init__(self, editors: EditorsResource) -> None:
        self._editors = editors

        self.retrieve = to_raw_response_wrapper(
            editors.retrieve,
        )
        self.list = to_raw_response_wrapper(
            editors.list,
        )
        self.resolve_editor_url = to_raw_response_wrapper(
            editors.resolve_editor_url,
        )


class AsyncEditorsResourceWithRawResponse:
    def __init__(self, editors: AsyncEditorsResource) -> None:
        self._editors = editors

        self.retrieve = async_to_raw_response_wrapper(
            editors.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            editors.list,
        )
        self.resolve_editor_url = async_to_raw_response_wrapper(
            editors.resolve_editor_url,
        )


class EditorsResourceWithStreamingResponse:
    def __init__(self, editors: EditorsResource) -> None:
        self._editors = editors

        self.retrieve = to_streamed_response_wrapper(
            editors.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            editors.list,
        )
        self.resolve_editor_url = to_streamed_response_wrapper(
            editors.resolve_editor_url,
        )


class AsyncEditorsResourceWithStreamingResponse:
    def __init__(self, editors: AsyncEditorsResource) -> None:
        self._editors = editors

        self.retrieve = async_to_streamed_response_wrapper(
            editors.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            editors.list,
        )
        self.resolve_editor_url = async_to_streamed_response_wrapper(
            editors.resolve_editor_url,
        )
