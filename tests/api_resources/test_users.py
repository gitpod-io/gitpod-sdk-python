# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import UserGetAuthenticatedUserResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_authenticated_user(self, client: Gitpod) -> None:
        user = client.users.get_authenticated_user()
        assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_authenticated_user_with_all_params(self, client: Gitpod) -> None:
        user = client.users.get_authenticated_user(
            empty=True,
        )
        assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_authenticated_user(self, client: Gitpod) -> None:
        response = client.users.with_raw_response.get_authenticated_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_authenticated_user(self, client: Gitpod) -> None:
        with client.users.with_streaming_response.get_authenticated_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_set_suspended(self, client: Gitpod) -> None:
        user = client.users.set_suspended()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_suspended_with_all_params(self, client: Gitpod) -> None:
        user = client.users.set_suspended(
            suspended=False,
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_suspended(self, client: Gitpod) -> None:
        response = client.users.with_raw_response.set_suspended()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_suspended(self, client: Gitpod) -> None:
        with client.users.with_streaming_response.set_suspended() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_authenticated_user(self, async_client: AsyncGitpod) -> None:
        user = await async_client.users.get_authenticated_user()
        assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_authenticated_user_with_all_params(self, async_client: AsyncGitpod) -> None:
        user = await async_client.users.get_authenticated_user(
            empty=True,
        )
        assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_authenticated_user(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.with_raw_response.get_authenticated_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_authenticated_user(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.with_streaming_response.get_authenticated_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetAuthenticatedUserResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_suspended(self, async_client: AsyncGitpod) -> None:
        user = await async_client.users.set_suspended()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_suspended_with_all_params(self, async_client: AsyncGitpod) -> None:
        user = await async_client.users.set_suspended(
            suspended=False,
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_suspended(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.with_raw_response.set_suspended()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_suspended(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.with_streaming_response.set_suspended() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True
