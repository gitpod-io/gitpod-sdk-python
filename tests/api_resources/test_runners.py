# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    RunnerListResponse,
    RunnerCreateResponse,
    RunnerRetrieveResponse,
    RunnerParseContextURLResponse,
    RunnerCreateRunnerTokenResponse,
    RunnerCheckAuthenticationForHostResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        runner = client.runners.create(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.create(
            connect_protocol_version=1,
            kind="RUNNER_KIND_UNSPECIFIED",
            name="xxx",
            provider="RUNNER_PROVIDER_UNSPECIFIED",
            spec={
                "configuration": {
                    "auto_update": True,
                    "region": "region",
                    "release_channel": "RUNNER_RELEASE_CHANNEL_UNSPECIFIED",
                },
                "desired_phase": "RUNNER_PHASE_UNSPECIFIED",
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerCreateResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        runner = client.runners.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        runner = client.runners.update(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.update(
            body={
                "name": "xxx",
                "runnerId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "spec": {},
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.update(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.update(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        runner = client.runners.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerListResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        runner = client.runners.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.delete(
            connect_protocol_version=1,
            force=True,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check_authentication_for_host(self, client: Gitpod) -> None:
        runner = client.runners.check_authentication_for_host(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    def test_method_check_authentication_for_host_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.check_authentication_for_host(
            connect_protocol_version=1,
            host="host",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_check_authentication_for_host(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.check_authentication_for_host(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_check_authentication_for_host(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.check_authentication_for_host(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_runner_token(self, client: Gitpod) -> None:
        runner = client.runners.create_runner_token(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    def test_method_create_runner_token_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.create_runner_token(
            connect_protocol_version=1,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_create_runner_token(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.create_runner_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_create_runner_token(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.create_runner_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_parse_context_url(self, client: Gitpod) -> None:
        runner = client.runners.parse_context_url(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    def test_method_parse_context_url_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.parse_context_url(
            connect_protocol_version=1,
            context_url="https://example.com",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_parse_context_url(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.parse_context_url(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_parse_context_url(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.parse_context_url(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRunners:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create(
            connect_protocol_version=1,
            kind="RUNNER_KIND_UNSPECIFIED",
            name="xxx",
            provider="RUNNER_PROVIDER_UNSPECIFIED",
            spec={
                "configuration": {
                    "auto_update": True,
                    "region": "region",
                    "release_channel": "RUNNER_RELEASE_CHANNEL_UNSPECIFIED",
                },
                "desired_phase": "RUNNER_PHASE_UNSPECIFIED",
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerCreateResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.update(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.update(
            body={
                "name": "xxx",
                "runnerId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "spec": {},
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.update(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.update(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerListResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.delete(
            connect_protocol_version=1,
            force=True,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check_authentication_for_host(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.check_authentication_for_host(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    async def test_method_check_authentication_for_host_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.check_authentication_for_host(
            connect_protocol_version=1,
            host="host",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_check_authentication_for_host(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.check_authentication_for_host(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_check_authentication_for_host(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.check_authentication_for_host(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_runner_token(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create_runner_token(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    async def test_method_create_runner_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create_runner_token(
            connect_protocol_version=1,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_create_runner_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.create_runner_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_create_runner_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.create_runner_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_parse_context_url(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.parse_context_url(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    async def test_method_parse_context_url_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.parse_context_url(
            connect_protocol_version=1,
            context_url="https://example.com",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_parse_context_url(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.parse_context_url(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_parse_context_url(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.parse_context_url(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True
