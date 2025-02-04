# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import EventListResponse, EventWatchResponse
from gitpod._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        event = client.events.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        event = client.events.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.events.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.events.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventListResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_watch_overload_1(self, client: Gitpod) -> None:
        event = client.events.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
        )
        assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_watch_with_all_params_overload_1(self, client: Gitpod) -> None:
        event = client.events.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_raw_response_watch_overload_1(self, client: Gitpod) -> None:
        response = client.events.with_raw_response.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_streaming_response_watch_overload_1(self, client: Gitpod) -> None:
        with client.events.with_streaming_response.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_watch_overload_2(self, client: Gitpod) -> None:
        event = client.events.watch(
            organization=True,
            connect_protocol_version=1,
        )
        assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_watch_with_all_params_overload_2(self, client: Gitpod) -> None:
        event = client.events.watch(
            organization=True,
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_raw_response_watch_overload_2(self, client: Gitpod) -> None:
        response = client.events.with_raw_response.watch(
            organization=True,
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_streaming_response_watch_overload_2(self, client: Gitpod) -> None:
        with client.events.with_streaming_response.watch(
            organization=True,
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(JSONLDecoder[EventWatchResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.events.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.events.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventListResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_watch_overload_1(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
        )
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_watch_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_raw_response_watch_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.events.with_raw_response.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_streaming_response_watch_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.events.with_streaming_response.watch(
            environment_id="environmentId",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_watch_overload_2(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.watch(
            organization=True,
            connect_protocol_version=1,
        )
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_watch_with_all_params_overload_2(self, async_client: AsyncGitpod) -> None:
        event = await async_client.events.watch(
            organization=True,
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_raw_response_watch_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.events.with_raw_response.watch(
            organization=True,
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_streaming_response_watch_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.events.with_streaming_response.watch(
            organization=True,
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncJSONLDecoder[EventWatchResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True
