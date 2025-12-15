# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncTokensPage, AsyncTokensPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.shared_params.subject import Subject
from ....types.runners.configurations import (
    HostAuthenticationTokenSource,
    host_authentication_token_list_params,
    host_authentication_token_create_params,
    host_authentication_token_delete_params,
    host_authentication_token_update_params,
    host_authentication_token_retrieve_params,
)
from ....types.runners.configurations.host_authentication_token import HostAuthenticationToken
from ....types.runners.configurations.host_authentication_token_source import HostAuthenticationTokenSource
from ....types.runners.configurations.host_authentication_token_create_response import (
    HostAuthenticationTokenCreateResponse,
)
from ....types.runners.configurations.host_authentication_token_retrieve_response import (
    HostAuthenticationTokenRetrieveResponse,
)

__all__ = ["HostAuthenticationTokensResource", "AsyncHostAuthenticationTokensResource"]


class HostAuthenticationTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostAuthenticationTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return HostAuthenticationTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostAuthenticationTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return HostAuthenticationTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        token: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        host: str | Omit = omit,
        integration_id: str | Omit = omit,
        refresh_token: str | Omit = omit,
        runner_id: str | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        source: HostAuthenticationTokenSource | Omit = omit,
        subject: Subject | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostAuthenticationTokenCreateResponse:
        """
        Creates a new authentication token for accessing remote hosts.

        Use this method to:

        - Set up SCM authentication
        - Configure OAuth credentials
        - Manage PAT tokens

        ### Examples

        - Create OAuth token:

          Creates a new OAuth-based authentication token.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          host: "github.com"
          token: "gho_xxxxxxxxxxxx"
          source: HOST_AUTHENTICATION_TOKEN_SOURCE_OAUTH
          expiresAt: "2024-12-31T23:59:59Z"
          refreshToken: "ghr_xxxxxxxxxxxx"
          ```

        Args:
          token: stored encrypted, retrieved via GetHostAuthenticationTokenValue

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

          refresh_token: stored encrypted, retrieved via GetHostAuthenticationTokenValue

          scopes: Maximum 100 scopes allowed (101 for validation purposes)

          subject: Subject identifies the principal (user or service account) for the token

          user_id: Deprecated: Use principal_id and principal_type instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/CreateHostAuthenticationToken",
            body=maybe_transform(
                {
                    "token": token,
                    "expires_at": expires_at,
                    "host": host,
                    "integration_id": integration_id,
                    "refresh_token": refresh_token,
                    "runner_id": runner_id,
                    "scopes": scopes,
                    "source": source,
                    "subject": subject,
                    "user_id": user_id,
                },
                host_authentication_token_create_params.HostAuthenticationTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostAuthenticationTokenRetrieveResponse:
        """
        Gets details about a specific host authentication token.

        Use this method to:

        - View token information
        - Check token expiration
        - Verify token validity

        ### Examples

        - Get token details:

          Retrieves information about a specific token.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

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

    def update(
        self,
        *,
        id: str | Omit = omit,
        token: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        refresh_token: Optional[str] | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates an existing host authentication token.

        Use this method to:

        - Refresh token values
        - Update expiration
        - Modify token settings

        ### Examples

        - Update token:

          Updates token value and expiration.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          token: "gho_xxxxxxxxxxxx"
          expiresAt: "2024-12-31T23:59:59Z"
          refreshToken: "ghr_xxxxxxxxxxxx"
          ```

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
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken",
            body=maybe_transform(
                {
                    "id": id,
                    "token": token,
                    "expires_at": expires_at,
                    "refresh_token": refresh_token,
                    "scopes": scopes,
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
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: host_authentication_token_list_params.Filter | Omit = omit,
        pagination: host_authentication_token_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncTokensPage[HostAuthenticationToken]:
        """
        Lists host authentication tokens with optional filtering.

        Use this method to:

        - View all tokens
        - Filter by runner or user
        - Monitor token status

        ### Examples

        - List all tokens:

          Shows all tokens with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - Filter by runner:

          Lists tokens for a specific runner.

          ```yaml
          filter:
            runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens",
            page=SyncTokensPage[HostAuthenticationToken],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                host_authentication_token_list_params.HostAuthenticationTokenListParams,
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
                    host_authentication_token_list_params.HostAuthenticationTokenListParams,
                ),
            ),
            model=HostAuthenticationToken,
            method="post",
        )

    def delete(
        self,
        *,
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a host authentication token.

        Use this method to:

        - Remove unused tokens
        - Revoke access
        - Clean up expired tokens

        ### Examples

        - Delete token:

          Permanently removes a token.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

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

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostAuthenticationTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostAuthenticationTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncHostAuthenticationTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        token: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        host: str | Omit = omit,
        integration_id: str | Omit = omit,
        refresh_token: str | Omit = omit,
        runner_id: str | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        source: HostAuthenticationTokenSource | Omit = omit,
        subject: Subject | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostAuthenticationTokenCreateResponse:
        """
        Creates a new authentication token for accessing remote hosts.

        Use this method to:

        - Set up SCM authentication
        - Configure OAuth credentials
        - Manage PAT tokens

        ### Examples

        - Create OAuth token:

          Creates a new OAuth-based authentication token.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          host: "github.com"
          token: "gho_xxxxxxxxxxxx"
          source: HOST_AUTHENTICATION_TOKEN_SOURCE_OAUTH
          expiresAt: "2024-12-31T23:59:59Z"
          refreshToken: "ghr_xxxxxxxxxxxx"
          ```

        Args:
          token: stored encrypted, retrieved via GetHostAuthenticationTokenValue

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

          refresh_token: stored encrypted, retrieved via GetHostAuthenticationTokenValue

          scopes: Maximum 100 scopes allowed (101 for validation purposes)

          subject: Subject identifies the principal (user or service account) for the token

          user_id: Deprecated: Use principal_id and principal_type instead

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/CreateHostAuthenticationToken",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "expires_at": expires_at,
                    "host": host,
                    "integration_id": integration_id,
                    "refresh_token": refresh_token,
                    "runner_id": runner_id,
                    "scopes": scopes,
                    "source": source,
                    "subject": subject,
                    "user_id": user_id,
                },
                host_authentication_token_create_params.HostAuthenticationTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostAuthenticationTokenRetrieveResponse:
        """
        Gets details about a specific host authentication token.

        Use this method to:

        - View token information
        - Check token expiration
        - Verify token validity

        ### Examples

        - Get token details:

          Retrieves information about a specific token.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

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

    async def update(
        self,
        *,
        id: str | Omit = omit,
        token: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        refresh_token: Optional[str] | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates an existing host authentication token.

        Use this method to:

        - Refresh token values
        - Update expiration
        - Modify token settings

        ### Examples

        - Update token:

          Updates token value and expiration.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          token: "gho_xxxxxxxxxxxx"
          expiresAt: "2024-12-31T23:59:59Z"
          refreshToken: "ghr_xxxxxxxxxxxx"
          ```

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
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "token": token,
                    "expires_at": expires_at,
                    "refresh_token": refresh_token,
                    "scopes": scopes,
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
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: host_authentication_token_list_params.Filter | Omit = omit,
        pagination: host_authentication_token_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[HostAuthenticationToken, AsyncTokensPage[HostAuthenticationToken]]:
        """
        Lists host authentication tokens with optional filtering.

        Use this method to:

        - View all tokens
        - Filter by runner or user
        - Monitor token status

        ### Examples

        - List all tokens:

          Shows all tokens with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - Filter by runner:

          Lists tokens for a specific runner.

          ```yaml
          filter:
            runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens",
            page=AsyncTokensPage[HostAuthenticationToken],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                host_authentication_token_list_params.HostAuthenticationTokenListParams,
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
                    host_authentication_token_list_params.HostAuthenticationTokenListParams,
                ),
            ),
            model=HostAuthenticationToken,
            method="post",
        )

    async def delete(
        self,
        *,
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a host authentication token.

        Use this method to:

        - Remove unused tokens
        - Revoke access
        - Clean up expired tokens

        ### Examples

        - Delete token:

          Permanently removes a token.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

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
