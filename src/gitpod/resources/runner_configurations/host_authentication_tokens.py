# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.runner_configurations import (
    host_authentication_token_list_params,
    host_authentication_token_create_params,
    host_authentication_token_delete_params,
    host_authentication_token_update_params,
    host_authentication_token_retrieve_params,
)
from ...types.runner_configurations.host_authentication_token_list_response import HostAuthenticationTokenListResponse
from ...types.runner_configurations.host_authentication_token_create_response import (
    HostAuthenticationTokenCreateResponse,
)
from ...types.runner_configurations.host_authentication_token_retrieve_response import (
    HostAuthenticationTokenRetrieveResponse,
)

__all__ = ["HostAuthenticationTokensResource", "AsyncHostAuthenticationTokensResource"]


class HostAuthenticationTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostAuthenticationTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return HostAuthenticationTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostAuthenticationTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return HostAuthenticationTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenCreateResponse:
        """
        GetHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            body=maybe_transform(
                {"id": id}, host_authentication_token_create_params.HostAuthenticationTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenRetrieveResponse:
        """
        GetHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            body=maybe_transform(
                {"id": id}, host_authentication_token_retrieve_params.HostAuthenticationTokenRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenRetrieveResponse,
        )

    @overload
    def update(
        self,
        *,
        expires_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

        Args:
          expires_at: A Timestamp represents a point in time independent of any time zone or local

              calendar, encoded as a count of seconds and fractions of seconds at nanosecond
              resolution. The count is relative to an epoch at UTC midnight on January 1,
              1970, in the proleptic Gregorian calendar which extends the Gregorian calendar
              backwards to year one.

              All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap
              second table is needed for interpretation, using a
              [24-hour linear smear](https://developers.google.com/time/smear).

              The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By
              restricting to that range, we ensure that we can convert to and from
              [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings.

              # Examples

              Example 1: Compute Timestamp from POSIX `time()`.

                   Timestamp timestamp;
                   timestamp.set_seconds(time(NULL));
                   timestamp.set_nanos(0);

              Example 2: Compute Timestamp from POSIX `gettimeofday()`.

                   struct timeval tv;
                   gettimeofday(&tv, NULL);

                   Timestamp timestamp;
                   timestamp.set_seconds(tv.tv_sec);
                   timestamp.set_nanos(tv.tv_usec * 1000);

              Example 3: Compute Timestamp from Win32 `GetSystemTimeAsFileTime()`.

                   FILETIME ft;
                   GetSystemTimeAsFileTime(&ft);
                   UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

                   // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
                   // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
                   Timestamp timestamp;
                   timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
                   timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

              Example 4: Compute Timestamp from Java `System.currentTimeMillis()`.

                   long millis = System.currentTimeMillis();

                   Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
                       .setNanos((int) ((millis % 1000) * 1000000)).build();

              Example 5: Compute Timestamp from Java `Instant.now()`.

                   Instant now = Instant.now();

                   Timestamp timestamp =
                       Timestamp.newBuilder().setSeconds(now.getEpochSecond())
                           .setNanos(now.getNano()).build();

              Example 6: Compute Timestamp from current time in Python.

                   timestamp = Timestamp()
                   timestamp.GetCurrentTime()

              # JSON Mapping

              In JSON format, the Timestamp type is encoded as a string in the
              [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the format is
              "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where {year} is always
              expressed using four digits while {month}, {day}, {hour}, {min}, and {sec} are
              zero-padded to two digits each. The fractional seconds, which can go up to 9
              digits (i.e. up to 1 nanosecond resolution), are optional. The "Z" suffix
              indicates the timezone ("UTC"); the timezone is required. A proto3 JSON
              serializer should always use UTC (as indicated by "Z") when printing the
              Timestamp type and a proto3 JSON parser should be able to accept both UTC and
              other timezones (as indicated by an offset).

              For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30 UTC on
              January 15, 2017.

              In JavaScript, one can convert a Date object to this format using the standard
              [toISOString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
              method. In Python, a standard `datetime.datetime` object can be converted to
              this format using
              [`strftime`](https://docs.python.org/2/library/time.html#time.strftime) with the
              time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java, one can use the
              Joda Time's
              [`ISODateTimeFormat.dateTime()`](<http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime()>)
              to obtain a formatter capable of generating timestamps in this format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["expires_at"], ["refresh_token"], ["token"])
    def update(
        self,
        *,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        refresh_token: str | NotGiven = NOT_GIVEN,
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken",
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "refresh_token": refresh_token,
                    "token": token,
                },
                host_authentication_token_update_params.HostAuthenticationTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        filter: host_authentication_token_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: host_authentication_token_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenListResponse:
        """
        ListHostAuthenticationTokens

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                host_authentication_token_list_params.HostAuthenticationTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenListResponse,
        )

    def delete(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken",
            body=maybe_transform(
                {"id": id}, host_authentication_token_delete_params.HostAuthenticationTokenDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHostAuthenticationTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostAuthenticationTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostAuthenticationTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostAuthenticationTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncHostAuthenticationTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenCreateResponse:
        """
        GetHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            body=await async_maybe_transform(
                {"id": id}, host_authentication_token_create_params.HostAuthenticationTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenRetrieveResponse:
        """
        GetHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            body=await async_maybe_transform(
                {"id": id}, host_authentication_token_retrieve_params.HostAuthenticationTokenRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenRetrieveResponse,
        )

    @overload
    async def update(
        self,
        *,
        expires_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

        Args:
          expires_at: A Timestamp represents a point in time independent of any time zone or local

              calendar, encoded as a count of seconds and fractions of seconds at nanosecond
              resolution. The count is relative to an epoch at UTC midnight on January 1,
              1970, in the proleptic Gregorian calendar which extends the Gregorian calendar
              backwards to year one.

              All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap
              second table is needed for interpretation, using a
              [24-hour linear smear](https://developers.google.com/time/smear).

              The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By
              restricting to that range, we ensure that we can convert to and from
              [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings.

              # Examples

              Example 1: Compute Timestamp from POSIX `time()`.

                   Timestamp timestamp;
                   timestamp.set_seconds(time(NULL));
                   timestamp.set_nanos(0);

              Example 2: Compute Timestamp from POSIX `gettimeofday()`.

                   struct timeval tv;
                   gettimeofday(&tv, NULL);

                   Timestamp timestamp;
                   timestamp.set_seconds(tv.tv_sec);
                   timestamp.set_nanos(tv.tv_usec * 1000);

              Example 3: Compute Timestamp from Win32 `GetSystemTimeAsFileTime()`.

                   FILETIME ft;
                   GetSystemTimeAsFileTime(&ft);
                   UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

                   // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
                   // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
                   Timestamp timestamp;
                   timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
                   timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

              Example 4: Compute Timestamp from Java `System.currentTimeMillis()`.

                   long millis = System.currentTimeMillis();

                   Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
                       .setNanos((int) ((millis % 1000) * 1000000)).build();

              Example 5: Compute Timestamp from Java `Instant.now()`.

                   Instant now = Instant.now();

                   Timestamp timestamp =
                       Timestamp.newBuilder().setSeconds(now.getEpochSecond())
                           .setNanos(now.getNano()).build();

              Example 6: Compute Timestamp from current time in Python.

                   timestamp = Timestamp()
                   timestamp.GetCurrentTime()

              # JSON Mapping

              In JSON format, the Timestamp type is encoded as a string in the
              [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the format is
              "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where {year} is always
              expressed using four digits while {month}, {day}, {hour}, {min}, and {sec} are
              zero-padded to two digits each. The fractional seconds, which can go up to 9
              digits (i.e. up to 1 nanosecond resolution), are optional. The "Z" suffix
              indicates the timezone ("UTC"); the timezone is required. A proto3 JSON
              serializer should always use UTC (as indicated by "Z") when printing the
              Timestamp type and a proto3 JSON parser should be able to accept both UTC and
              other timezones (as indicated by an offset).

              For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30 UTC on
              January 15, 2017.

              In JavaScript, one can convert a Date object to this format using the standard
              [toISOString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
              method. In Python, a standard `datetime.datetime` object can be converted to
              this format using
              [`strftime`](https://docs.python.org/2/library/time.html#time.strftime) with the
              time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java, one can use the
              Joda Time's
              [`ISODateTimeFormat.dateTime()`](<http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime()>)
              to obtain a formatter capable of generating timestamps in this format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["expires_at"], ["refresh_token"], ["token"])
    async def update(
        self,
        *,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        refresh_token: str | NotGiven = NOT_GIVEN,
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken",
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "refresh_token": refresh_token,
                    "token": token,
                },
                host_authentication_token_update_params.HostAuthenticationTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        filter: host_authentication_token_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: host_authentication_token_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenListResponse:
        """
        ListHostAuthenticationTokens

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                host_authentication_token_list_params.HostAuthenticationTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenListResponse,
        )

    async def delete(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteHostAuthenticationToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken",
            body=await async_maybe_transform(
                {"id": id}, host_authentication_token_delete_params.HostAuthenticationTokenDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HostAuthenticationTokensResourceWithRawResponse:
    def __init__(self, host_authentication_tokens: HostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = to_raw_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = to_raw_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = to_raw_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = to_raw_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            host_authentication_tokens.delete,
        )


class AsyncHostAuthenticationTokensResourceWithRawResponse:
    def __init__(self, host_authentication_tokens: AsyncHostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = async_to_raw_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = async_to_raw_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            host_authentication_tokens.delete,
        )


class HostAuthenticationTokensResourceWithStreamingResponse:
    def __init__(self, host_authentication_tokens: HostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = to_streamed_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = to_streamed_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            host_authentication_tokens.delete,
        )


class AsyncHostAuthenticationTokensResourceWithStreamingResponse:
    def __init__(self, host_authentication_tokens: AsyncHostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = async_to_streamed_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = async_to_streamed_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            host_authentication_tokens.delete,
        )
