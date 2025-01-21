# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import automations_file_upsert_params
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
from ..types.automations_file_upsert_response import AutomationsFileUpsertResponse

__all__ = ["AutomationsFilesResource", "AsyncAutomationsFilesResource"]


class AutomationsFilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomationsFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AutomationsFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationsFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AutomationsFilesResourceWithStreamingResponse(self)

    def upsert(
        self,
        *,
        connect_protocol_version: Literal[1],
        automations_file: automations_file_upsert_params.AutomationsFile | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutomationsFileUpsertResponse:
        """
        UpsertAutomationsFile upserts the automations file for the given environment.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          automations_file: WARN: Do not remove any field here, as it will break reading automation yaml
              files. We error if there are any unknown fields in the yaml (to ensure the yaml
              is correct), but would break if we removed any fields. This includes marking a
              field as "reserved" in the proto file, this will also break reading the yaml.

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
            "/gitpod.v1.EnvironmentAutomationService/UpsertAutomationsFile",
            body=maybe_transform(
                {
                    "automations_file": automations_file,
                    "environment_id": environment_id,
                },
                automations_file_upsert_params.AutomationsFileUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationsFileUpsertResponse,
        )


class AsyncAutomationsFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomationsFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationsFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationsFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncAutomationsFilesResourceWithStreamingResponse(self)

    async def upsert(
        self,
        *,
        connect_protocol_version: Literal[1],
        automations_file: automations_file_upsert_params.AutomationsFile | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutomationsFileUpsertResponse:
        """
        UpsertAutomationsFile upserts the automations file for the given environment.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          automations_file: WARN: Do not remove any field here, as it will break reading automation yaml
              files. We error if there are any unknown fields in the yaml (to ensure the yaml
              is correct), but would break if we removed any fields. This includes marking a
              field as "reserved" in the proto file, this will also break reading the yaml.

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
            "/gitpod.v1.EnvironmentAutomationService/UpsertAutomationsFile",
            body=await async_maybe_transform(
                {
                    "automations_file": automations_file,
                    "environment_id": environment_id,
                },
                automations_file_upsert_params.AutomationsFileUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationsFileUpsertResponse,
        )


class AutomationsFilesResourceWithRawResponse:
    def __init__(self, automations_files: AutomationsFilesResource) -> None:
        self._automations_files = automations_files

        self.upsert = to_raw_response_wrapper(
            automations_files.upsert,
        )


class AsyncAutomationsFilesResourceWithRawResponse:
    def __init__(self, automations_files: AsyncAutomationsFilesResource) -> None:
        self._automations_files = automations_files

        self.upsert = async_to_raw_response_wrapper(
            automations_files.upsert,
        )


class AutomationsFilesResourceWithStreamingResponse:
    def __init__(self, automations_files: AutomationsFilesResource) -> None:
        self._automations_files = automations_files

        self.upsert = to_streamed_response_wrapper(
            automations_files.upsert,
        )


class AsyncAutomationsFilesResourceWithStreamingResponse:
    def __init__(self, automations_files: AsyncAutomationsFilesResource) -> None:
        self._automations_files = automations_files

        self.upsert = async_to_streamed_response_wrapper(
            automations_files.upsert,
        )
