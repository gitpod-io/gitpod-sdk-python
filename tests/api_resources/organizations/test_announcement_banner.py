# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.organizations import (
    AnnouncementBannerGetResponse,
    AnnouncementBannerUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnouncementBanner:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        announcement_banner = client.organizations.announcement_banner.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        announcement_banner = client.organizations.announcement_banner.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            enabled=False,
            message="message",
        )
        assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.announcement_banner.with_raw_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        announcement_banner = response.parse()
        assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.announcement_banner.with_streaming_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            announcement_banner = response.parse()
            assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Gitpod) -> None:
        announcement_banner = client.organizations.announcement_banner.get(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AnnouncementBannerGetResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Gitpod) -> None:
        response = client.organizations.announcement_banner.with_raw_response.get(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        announcement_banner = response.parse()
        assert_matches_type(AnnouncementBannerGetResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Gitpod) -> None:
        with client.organizations.announcement_banner.with_streaming_response.get(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            announcement_banner = response.parse()
            assert_matches_type(AnnouncementBannerGetResponse, announcement_banner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnnouncementBanner:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        announcement_banner = await async_client.organizations.announcement_banner.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        announcement_banner = await async_client.organizations.announcement_banner.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            enabled=False,
            message="message",
        )
        assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.announcement_banner.with_raw_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        announcement_banner = await response.parse()
        assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.announcement_banner.with_streaming_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            announcement_banner = await response.parse()
            assert_matches_type(AnnouncementBannerUpdateResponse, announcement_banner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncGitpod) -> None:
        announcement_banner = await async_client.organizations.announcement_banner.get(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AnnouncementBannerGetResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.announcement_banner.with_raw_response.get(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        announcement_banner = await response.parse()
        assert_matches_type(AnnouncementBannerGetResponse, announcement_banner, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.announcement_banner.with_streaming_response.get(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            announcement_banner = await response.parse()
            assert_matches_type(AnnouncementBannerGetResponse, announcement_banner, path=["response"])

        assert cast(Any, response.is_closed) is True
