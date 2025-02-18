# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Editor,
    EditorRetrieveResponse,
    EditorResolveURLResponse,
)
from gitpod.pagination import SyncEditorsPage, AsyncEditorsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEditors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        editor = client.editors.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.editors.with_raw_response.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = response.parse()
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.editors.with_streaming_response.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = response.parse()
            assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        editor = client.editors.list()
        assert_matches_type(SyncEditorsPage[Editor], editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        editor = client.editors.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncEditorsPage[Editor], editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.editors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = response.parse()
        assert_matches_type(SyncEditorsPage[Editor], editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.editors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = response.parse()
            assert_matches_type(SyncEditorsPage[Editor], editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_resolve_url(self, client: Gitpod) -> None:
        editor = client.editors.resolve_url(
            editor_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(EditorResolveURLResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_resolve_url(self, client: Gitpod) -> None:
        response = client.editors.with_raw_response.resolve_url(
            editor_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = response.parse()
        assert_matches_type(EditorResolveURLResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_resolve_url(self, client: Gitpod) -> None:
        with client.editors.with_streaming_response.resolve_url(
            editor_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = response.parse()
            assert_matches_type(EditorResolveURLResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEditors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.editors.with_raw_response.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = await response.parse()
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.editors.with_streaming_response.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = await response.parse()
            assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.list()
        assert_matches_type(AsyncEditorsPage[Editor], editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncEditorsPage[Editor], editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.editors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = await response.parse()
        assert_matches_type(AsyncEditorsPage[Editor], editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.editors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = await response.parse()
            assert_matches_type(AsyncEditorsPage[Editor], editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_resolve_url(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.resolve_url(
            editor_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(EditorResolveURLResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_resolve_url(self, async_client: AsyncGitpod) -> None:
        response = await async_client.editors.with_raw_response.resolve_url(
            editor_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = await response.parse()
        assert_matches_type(EditorResolveURLResponse, editor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_resolve_url(self, async_client: AsyncGitpod) -> None:
        async with async_client.editors.with_streaming_response.resolve_url(
            editor_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = await response.parse()
            assert_matches_type(EditorResolveURLResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True
