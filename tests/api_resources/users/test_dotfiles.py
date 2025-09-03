# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.users import DotfileGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDotfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Gitpod) -> None:
        dotfile = client.users.dotfiles.get()
        assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Gitpod) -> None:
        dotfile = client.users.dotfiles.get(
            empty=True,
        )
        assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Gitpod) -> None:
        response = client.users.dotfiles.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dotfile = response.parse()
        assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Gitpod) -> None:
        with client.users.dotfiles.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dotfile = response.parse()
            assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set(self, client: Gitpod) -> None:
        dotfile = client.users.dotfiles.set()
        assert_matches_type(object, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: Gitpod) -> None:
        dotfile = client.users.dotfiles.set(
            repository="https://example.com",
        )
        assert_matches_type(object, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Gitpod) -> None:
        response = client.users.dotfiles.with_raw_response.set()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dotfile = response.parse()
        assert_matches_type(object, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Gitpod) -> None:
        with client.users.dotfiles.with_streaming_response.set() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dotfile = response.parse()
            assert_matches_type(object, dotfile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDotfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncGitpod) -> None:
        dotfile = await async_client.users.dotfiles.get()
        assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncGitpod) -> None:
        dotfile = await async_client.users.dotfiles.get(
            empty=True,
        )
        assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.dotfiles.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dotfile = await response.parse()
        assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.dotfiles.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dotfile = await response.parse()
            assert_matches_type(DotfileGetResponse, dotfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncGitpod) -> None:
        dotfile = await async_client.users.dotfiles.set()
        assert_matches_type(object, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncGitpod) -> None:
        dotfile = await async_client.users.dotfiles.set(
            repository="https://example.com",
        )
        assert_matches_type(object, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncGitpod) -> None:
        response = await async_client.users.dotfiles.with_raw_response.set()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dotfile = await response.parse()
        assert_matches_type(object, dotfile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncGitpod) -> None:
        async with async_client.users.dotfiles.with_streaming_response.set() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dotfile = await response.parse()
            assert_matches_type(object, dotfile, path=["response"])

        assert cast(Any, response.is_closed) is True
