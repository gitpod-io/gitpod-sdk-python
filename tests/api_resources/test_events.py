# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import EventListResponse, EventWatchResponse
from gitpod.pagination import SyncEntriesPage, AsyncEntriesPage
from gitpod._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        event = client.events.list()
        assert_matches_type(SyncEntriesPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        event = client.events.list(
            token="token",
            page_size=0,
            filter={
                "actor_ids": ["d2c94c27-3b76-4a42-b88c-95a85e392c68"],
                "actor_principals": ["PRINCIPAL_USER"],
                "subject_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "subject_types": ["RESOURCE_TYPE_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncEntriesPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncEntriesPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncEntriesPage[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_method_watch(self, client: Gitpod) -> None:
        event_stream = client.events.watch()
        assert_matches_type(JSONLDecoder[EventWatchResponse], event_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_method_watch_with_all_params(self, client: Gitpod) -> None:
        event_stream = client.events.watch(
            environment_id="environmentId",
            organization=True,
        )
        assert_matches_type(JSONLDecoder[EventWatchResponse], event_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_raw_response_watch(self, client: Gitpod) -> None:
        response = client.events.with_raw_response.watch()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_streaming_response_watch(self, client: Gitpod) -> None:
        with client.events.with_streaming_response.watch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.list()
        assert_matches_type(AsyncEntriesPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.list(
            token="token",
            page_size=0,
            filter={
                "actor_ids": ["d2c94c27-3b76-4a42-b88c-95a85e392c68"],
                "actor_principals": ["PRINCIPAL_USER"],
                "subject_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "subject_types": ["RESOURCE_TYPE_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncEntriesPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncEntriesPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncEntriesPage[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_method_watch(self, async_client: AsyncGitpod) -> None:
        event_stream = await async_client.events.watch()
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_method_watch_with_all_params(self, async_client: AsyncGitpod) -> None:
        event_stream = await async_client.events.watch(
            environment_id="environmentId",
            organization=True,
        )
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_raw_response_watch(self, async_client: AsyncGitpod) -> None:
        response = await async_client.events.with_raw_response.watch()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_streaming_response_watch(self, async_client: AsyncGitpod) -> None:
        async with async_client.events.with_streaming_response.watch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
