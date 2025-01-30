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
    RunnerGetRunnerResponse,
    RunnerParseContextURLResponse,
    RunnerCreateRunnerTokenResponse,
    RunnerCheckAuthenticationForHostResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        runner = client.runners.create()
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.create(
            kind="RUNNER_KIND_UNSPECIFIED",
            name="xxx",
            spec={
                "configuration": {
                    "auto_update": True,
                    "region": "region",
                    "release_channel": "RUNNER_RELEASE_CHANNEL_UNSPECIFIED",
                },
                "desired_phase": "RUNNER_PHASE_UNSPECIFIED",
            },
        )
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerCreateResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        runner = client.runners.retrieve()
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.retrieve(
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        runner = client.runners.list()
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.list(
            filter={
                "creator_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "kinds": ["RUNNER_KIND_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerListResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check_authentication_for_host(self, client: Gitpod) -> None:
        runner = client.runners.check_authentication_for_host()
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    def test_method_check_authentication_for_host_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.check_authentication_for_host(
            host="host",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_check_authentication_for_host(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.check_authentication_for_host()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_check_authentication_for_host(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.check_authentication_for_host() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_runner_token(self, client: Gitpod) -> None:
        runner = client.runners.create_runner_token()
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    def test_method_create_runner_token_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.create_runner_token(
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_create_runner_token(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.create_runner_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_create_runner_token(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.create_runner_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_runner(self, client: Gitpod) -> None:
        runner = client.runners.delete_runner()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_method_delete_runner_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.delete_runner(
            force=True,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_raw_response_delete_runner(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.delete_runner()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_streaming_response_delete_runner(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.delete_runner() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_runner(self, client: Gitpod) -> None:
        runner = client.runners.get_runner()
        assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

    @parametrize
    def test_method_get_runner_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.get_runner(
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_get_runner(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.get_runner()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_get_runner(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.get_runner() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_parse_context_url(self, client: Gitpod) -> None:
        runner = client.runners.parse_context_url()
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    def test_method_parse_context_url_with_all_params(self, client: Gitpod) -> None:
        runner = client.runners.parse_context_url(
            context_url="https://example.com",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    def test_raw_response_parse_context_url(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.parse_context_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    def test_streaming_response_parse_context_url(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.parse_context_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_runner_overload_1(self, client: Gitpod) -> None:
        runner = client.runners.update_runner(
            name="xxx",
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_raw_response_update_runner_overload_1(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.update_runner(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_streaming_response_update_runner_overload_1(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.update_runner(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_runner_overload_2(self, client: Gitpod) -> None:
        runner = client.runners.update_runner(
            spec={"configuration": {"auto_update": True}},
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_raw_response_update_runner_overload_2(self, client: Gitpod) -> None:
        response = client.runners.with_raw_response.update_runner(
            spec={"configuration": {"auto_update": True}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    def test_streaming_response_update_runner_overload_2(self, client: Gitpod) -> None:
        with client.runners.with_streaming_response.update_runner(
            spec={"configuration": {"auto_update": True}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRunners:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create()
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create(
            kind="RUNNER_KIND_UNSPECIFIED",
            name="xxx",
            spec={
                "configuration": {
                    "auto_update": True,
                    "region": "region",
                    "release_channel": "RUNNER_RELEASE_CHANNEL_UNSPECIFIED",
                },
                "desired_phase": "RUNNER_PHASE_UNSPECIFIED",
            },
        )
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerCreateResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerCreateResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.retrieve()
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.retrieve(
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerRetrieveResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.list()
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.list(
            filter={
                "creator_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "kinds": ["RUNNER_KIND_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerListResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerListResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check_authentication_for_host(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.check_authentication_for_host()
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    async def test_method_check_authentication_for_host_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.check_authentication_for_host(
            host="host",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_check_authentication_for_host(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.check_authentication_for_host()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_check_authentication_for_host(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.check_authentication_for_host() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerCheckAuthenticationForHostResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_runner_token(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create_runner_token()
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    async def test_method_create_runner_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.create_runner_token(
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_create_runner_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.create_runner_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_create_runner_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.create_runner_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerCreateRunnerTokenResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_runner(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.delete_runner()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_method_delete_runner_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.delete_runner(
            force=True,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_raw_response_delete_runner(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.delete_runner()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_streaming_response_delete_runner(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.delete_runner() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_runner(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.get_runner()
        assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

    @parametrize
    async def test_method_get_runner_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.get_runner(
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_get_runner(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.get_runner()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_get_runner(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.get_runner() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerGetRunnerResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_parse_context_url(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.parse_context_url()
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    async def test_method_parse_context_url_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.parse_context_url(
            context_url="https://example.com",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    async def test_raw_response_parse_context_url(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.parse_context_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

    @parametrize
    async def test_streaming_response_parse_context_url(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.parse_context_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(RunnerParseContextURLResponse, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_runner_overload_1(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.update_runner(
            name="xxx",
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_raw_response_update_runner_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.update_runner(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_streaming_response_update_runner_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.update_runner(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_runner_overload_2(self, async_client: AsyncGitpod) -> None:
        runner = await async_client.runners.update_runner(
            spec={"configuration": {"auto_update": True}},
        )
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_raw_response_update_runner_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.with_raw_response.update_runner(
            spec={"configuration": {"auto_update": True}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner = await response.parse()
        assert_matches_type(object, runner, path=["response"])

    @parametrize
    async def test_streaming_response_update_runner_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.with_streaming_response.update_runner(
            spec={"configuration": {"auto_update": True}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner = await response.parse()
            assert_matches_type(object, runner, path=["response"])

        assert cast(Any, response.is_closed) is True
