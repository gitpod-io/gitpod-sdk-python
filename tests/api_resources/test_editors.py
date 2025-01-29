# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    EditorListResponse,
    EditorRetrieveResponse,
    EditorResolveEditorURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEditors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        editor = client.editors.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        editor = client.editors.retrieve(
            connect_protocol_version=1,
            id="id",
            connect_timeout_ms=0,
        )
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.editors.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = response.parse()
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.editors.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = response.parse()
            assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        editor = client.editors.list(
            connect_protocol_version=1,
        )
        assert_matches_type(EditorListResponse, editor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        editor = client.editors.list(
            connect_protocol_version=1,
            pagination={
                "token": "token",
                "page_size": 0,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(EditorListResponse, editor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.editors.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = response.parse()
        assert_matches_type(EditorListResponse, editor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.editors.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = response.parse()
            assert_matches_type(EditorListResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_resolve_editor_url(self, client: Gitpod) -> None:
        editor = client.editors.resolve_editor_url(
            connect_protocol_version=1,
        )
        assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

    @parametrize
    def test_method_resolve_editor_url_with_all_params(self, client: Gitpod) -> None:
        editor = client.editors.resolve_editor_url(
            connect_protocol_version=1,
            editor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

    @parametrize
    def test_raw_response_resolve_editor_url(self, client: Gitpod) -> None:
        response = client.editors.with_raw_response.resolve_editor_url(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = response.parse()
        assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

    @parametrize
    def test_streaming_response_resolve_editor_url(self, client: Gitpod) -> None:
        with client.editors.with_streaming_response.resolve_editor_url(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = response.parse()
            assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEditors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.retrieve(
            connect_protocol_version=1,
            id="id",
            connect_timeout_ms=0,
        )
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.editors.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = await response.parse()
        assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.editors.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = await response.parse()
            assert_matches_type(EditorRetrieveResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.list(
            connect_protocol_version=1,
        )
        assert_matches_type(EditorListResponse, editor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.list(
            connect_protocol_version=1,
            pagination={
                "token": "token",
                "page_size": 0,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(EditorListResponse, editor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.editors.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = await response.parse()
        assert_matches_type(EditorListResponse, editor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.editors.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = await response.parse()
            assert_matches_type(EditorListResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_resolve_editor_url(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.resolve_editor_url(
            connect_protocol_version=1,
        )
        assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

    @parametrize
    async def test_method_resolve_editor_url_with_all_params(self, async_client: AsyncGitpod) -> None:
        editor = await async_client.editors.resolve_editor_url(
            connect_protocol_version=1,
            editor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

    @parametrize
    async def test_raw_response_resolve_editor_url(self, async_client: AsyncGitpod) -> None:
        response = await async_client.editors.with_raw_response.resolve_editor_url(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        editor = await response.parse()
        assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

    @parametrize
    async def test_streaming_response_resolve_editor_url(self, async_client: AsyncGitpod) -> None:
        async with async_client.editors.with_streaming_response.resolve_editor_url(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            editor = await response.parse()
            assert_matches_type(EditorResolveEditorURLResponse, editor, path=["response"])

        assert cast(Any, response.is_closed) is True
