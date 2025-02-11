# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import event_list_params, event_watch_params
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
from ..pagination import SyncEntriesPage, AsyncEntriesPage
from .._base_client import AsyncPaginator, make_request_options
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.event_list_response import EventListResponse
from ..types.event_watch_response import EventWatchResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: event_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: event_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesPage[EventListResponse]:
        """
        ListAuditLogs retrieves a paginated list of audit logs for the specified
        organization

        Args:
          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EventService/ListAuditLogs",
            page=SyncEntriesPage[EventListResponse],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                event_list_params.EventListParams,
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
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
            method="post",
        )

    def watch(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        organization: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JSONLDecoder[EventWatchResponse]:
        """
        WatchEvents streams all requests events to the client

        Args:
          environment_id: Environment scope produces events for the environment itself, all tasks, task
              executions, and services associated with that environment.

          organization: Organization scope produces events for all projects, runners and environments
              the caller can see within their organization. No task, task execution or service
              events are produed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        return self._post(
            "/gitpod.v1.EventService/WatchEvents",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "organization": organization,
                },
                event_watch_params.EventWatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[EventWatchResponse],
            stream=True,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: event_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: event_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventListResponse, AsyncEntriesPage[EventListResponse]]:
        """
        ListAuditLogs retrieves a paginated list of audit logs for the specified
        organization

        Args:
          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EventService/ListAuditLogs",
            page=AsyncEntriesPage[EventListResponse],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                event_list_params.EventListParams,
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
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
            method="post",
        )

    async def watch(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        organization: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncJSONLDecoder[EventWatchResponse]:
        """
        WatchEvents streams all requests events to the client

        Args:
          environment_id: Environment scope produces events for the environment itself, all tasks, task
              executions, and services associated with that environment.

          organization: Organization scope produces events for all projects, runners and environments
              the caller can see within their organization. No task, task execution or service
              events are produed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        return await self._post(
            "/gitpod.v1.EventService/WatchEvents",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "organization": organization,
                },
                event_watch_params.EventWatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[EventWatchResponse],
            stream=True,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.watch = to_raw_response_wrapper(
            events.watch,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.watch = async_to_raw_response_wrapper(
            events.watch,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.watch = to_streamed_response_wrapper(
            events.watch,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.watch = async_to_streamed_response_wrapper(
            events.watch,
        )
