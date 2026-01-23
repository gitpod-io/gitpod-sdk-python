# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organizations import announcement_banner_get_params, announcement_banner_update_params
from ...types.organizations.announcement_banner_get_response import AnnouncementBannerGetResponse
from ...types.organizations.announcement_banner_update_response import AnnouncementBannerUpdateResponse

__all__ = ["AnnouncementBannerResource", "AsyncAnnouncementBannerResource"]


class AnnouncementBannerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnouncementBannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AnnouncementBannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnouncementBannerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AnnouncementBannerResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        organization_id: str,
        enabled: Optional[bool] | Omit = omit,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnnouncementBannerUpdateResponse:
        """
        Updates the announcement banner configuration for an organization.

        Use this method to configure the announcement banner displayed to all users.
        Only organization admins can update the banner. Requires Enterprise tier.

        ### Examples

        - Enable announcement banner:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          message: "Scheduled maintenance on Saturday 10pm-2am UTC"
          enabled: true
          ```

        - Disable announcement banner:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          enabled: false
          ```

        Args:
          organization_id: organization_id is the ID of the organization

          enabled: enabled controls whether the banner is displayed

          message: message is the banner message. Supports basic Markdown. Maximum 1000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateAnnouncementBanner",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "enabled": enabled,
                    "message": message,
                },
                announcement_banner_update_params.AnnouncementBannerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnouncementBannerUpdateResponse,
        )

    def get(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnnouncementBannerGetResponse:
        """
        Retrieves the announcement banner configuration for an organization.

        Use this method to fetch the current announcement banner settings. All
        organization members can read the banner configuration.

        ### Examples

        - Get announcement banner:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetAnnouncementBanner",
            body=maybe_transform(
                {"organization_id": organization_id}, announcement_banner_get_params.AnnouncementBannerGetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnouncementBannerGetResponse,
        )


class AsyncAnnouncementBannerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnouncementBannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnnouncementBannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnouncementBannerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncAnnouncementBannerResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        organization_id: str,
        enabled: Optional[bool] | Omit = omit,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnnouncementBannerUpdateResponse:
        """
        Updates the announcement banner configuration for an organization.

        Use this method to configure the announcement banner displayed to all users.
        Only organization admins can update the banner. Requires Enterprise tier.

        ### Examples

        - Enable announcement banner:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          message: "Scheduled maintenance on Saturday 10pm-2am UTC"
          enabled: true
          ```

        - Disable announcement banner:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          enabled: false
          ```

        Args:
          organization_id: organization_id is the ID of the organization

          enabled: enabled controls whether the banner is displayed

          message: message is the banner message. Supports basic Markdown. Maximum 1000 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateAnnouncementBanner",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "enabled": enabled,
                    "message": message,
                },
                announcement_banner_update_params.AnnouncementBannerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnouncementBannerUpdateResponse,
        )

    async def get(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnnouncementBannerGetResponse:
        """
        Retrieves the announcement banner configuration for an organization.

        Use this method to fetch the current announcement banner settings. All
        organization members can read the banner configuration.

        ### Examples

        - Get announcement banner:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetAnnouncementBanner",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, announcement_banner_get_params.AnnouncementBannerGetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnouncementBannerGetResponse,
        )


class AnnouncementBannerResourceWithRawResponse:
    def __init__(self, announcement_banner: AnnouncementBannerResource) -> None:
        self._announcement_banner = announcement_banner

        self.update = to_raw_response_wrapper(
            announcement_banner.update,
        )
        self.get = to_raw_response_wrapper(
            announcement_banner.get,
        )


class AsyncAnnouncementBannerResourceWithRawResponse:
    def __init__(self, announcement_banner: AsyncAnnouncementBannerResource) -> None:
        self._announcement_banner = announcement_banner

        self.update = async_to_raw_response_wrapper(
            announcement_banner.update,
        )
        self.get = async_to_raw_response_wrapper(
            announcement_banner.get,
        )


class AnnouncementBannerResourceWithStreamingResponse:
    def __init__(self, announcement_banner: AnnouncementBannerResource) -> None:
        self._announcement_banner = announcement_banner

        self.update = to_streamed_response_wrapper(
            announcement_banner.update,
        )
        self.get = to_streamed_response_wrapper(
            announcement_banner.get,
        )


class AsyncAnnouncementBannerResourceWithStreamingResponse:
    def __init__(self, announcement_banner: AsyncAnnouncementBannerResource) -> None:
        self._announcement_banner = announcement_banner

        self.update = async_to_streamed_response_wrapper(
            announcement_banner.update,
        )
        self.get = async_to_streamed_response_wrapper(
            announcement_banner.get,
        )
