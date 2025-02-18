# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncPersonalAccessTokensPage, AsyncPersonalAccessTokensPage
from gitpod.types.users import PatGetResponse, PersonalAccessToken

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        pat = client.users.pats.list()
        assert_matches_type(SyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        pat = client.users.pats.list(
            token="token",
            page_size=0,
            filter={"user_ids": ["f53d2330-3795-4c5d-a1f3-453121af9c60"]},
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.users.pats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pat = response.parse()
        assert_matches_type(SyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.users.pats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pat = response.parse()
            assert_matches_type(SyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        pat = client.users.pats.delete()
        assert_matches_type(object, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        pat = client.users.pats.delete(
            personal_access_token_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.users.pats.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pat = response.parse()
        assert_matches_type(object, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.users.pats.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pat = response.parse()
            assert_matches_type(object, pat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Gitpod) -> None:
        pat = client.users.pats.get()
        assert_matches_type(PatGetResponse, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Gitpod) -> None:
        pat = client.users.pats.get(
            personal_access_token_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(PatGetResponse, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Gitpod) -> None:
        response = client.users.pats.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pat = response.parse()
        assert_matches_type(PatGetResponse, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Gitpod) -> None:
        with client.users.pats.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pat = response.parse()
            assert_matches_type(PatGetResponse, pat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        pat = await async_client.users.pats.list()
        assert_matches_type(AsyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        pat = await async_client.users.pats.list(
            token="token",
            page_size=0,
            filter={"user_ids": ["f53d2330-3795-4c5d-a1f3-453121af9c60"]},
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.pats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pat = await response.parse()
        assert_matches_type(AsyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.pats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pat = await response.parse()
            assert_matches_type(AsyncPersonalAccessTokensPage[PersonalAccessToken], pat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        pat = await async_client.users.pats.delete()
        assert_matches_type(object, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        pat = await async_client.users.pats.delete(
            personal_access_token_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.pats.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pat = await response.parse()
        assert_matches_type(object, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.pats.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pat = await response.parse()
            assert_matches_type(object, pat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncGitpod) -> None:
        pat = await async_client.users.pats.get()
        assert_matches_type(PatGetResponse, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGitpod) -> None:
        pat = await async_client.users.pats.get(
            personal_access_token_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(PatGetResponse, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.pats.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pat = await response.parse()
        assert_matches_type(PatGetResponse, pat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.pats.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pat = await response.parse()
            assert_matches_type(PatGetResponse, pat, path=["response"])

        assert cast(Any, response.is_closed) is True
