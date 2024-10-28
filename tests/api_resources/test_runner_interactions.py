# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    RunnerInteractionSignupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunnerInteractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_mark_active(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interactions.mark_active(
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_mark_active_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interactions.mark_active(
            connect_protocol_version=1,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_mark_active(self, client: Gitpod) -> None:
        response = client.runner_interactions.with_raw_response.mark_active(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_mark_active(self, client: Gitpod) -> None:
        with client.runner_interactions.with_streaming_response.mark_active(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signup(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interactions.signup(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

    @parametrize
    def test_method_signup_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interactions.signup(
            connect_protocol_version=1,
            environment_classes=[
                {
                    "id": "id",
                    "configuration": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ],
                    "description": "xxx",
                    "display_name": "xxx",
                    "enabled": True,
                    "runner_id": "runnerId",
                },
                {
                    "id": "id",
                    "configuration": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ],
                    "description": "xxx",
                    "display_name": "xxx",
                    "enabled": True,
                    "runner_id": "runnerId",
                },
                {
                    "id": "id",
                    "configuration": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ],
                    "description": "xxx",
                    "display_name": "xxx",
                    "enabled": True,
                    "runner_id": "runnerId",
                },
            ],
            public_key="U3RhaW5sZXNzIHJvY2tz",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_signup(self, client: Gitpod) -> None:
        response = client.runner_interactions.with_raw_response.signup(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_signup(self, client: Gitpod) -> None:
        with client.runner_interactions.with_streaming_response.signup(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_status(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interactions.update_status(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_update_status_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interactions.update_status(
            body={
                "additionalInfo": [{}, {}, {}],
                "degredationMessage": "degredationMessage",
                "logUrl": "https://example.com",
                "region": "region",
                "runnerId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "systemDetails": "systemDetails",
                "version": "version",
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Gitpod) -> None:
        response = client.runner_interactions.with_raw_response.update_status(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Gitpod) -> None:
        with client.runner_interactions.with_streaming_response.update_status(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRunnerInteractions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_mark_active(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interactions.mark_active(
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_mark_active_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interactions.mark_active(
            connect_protocol_version=1,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_mark_active(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interactions.with_raw_response.mark_active(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_mark_active(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interactions.with_streaming_response.mark_active(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signup(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interactions.signup(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_method_signup_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interactions.signup(
            connect_protocol_version=1,
            environment_classes=[
                {
                    "id": "id",
                    "configuration": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ],
                    "description": "xxx",
                    "display_name": "xxx",
                    "enabled": True,
                    "runner_id": "runnerId",
                },
                {
                    "id": "id",
                    "configuration": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ],
                    "description": "xxx",
                    "display_name": "xxx",
                    "enabled": True,
                    "runner_id": "runnerId",
                },
                {
                    "id": "id",
                    "configuration": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ],
                    "description": "xxx",
                    "display_name": "xxx",
                    "enabled": True,
                    "runner_id": "runnerId",
                },
            ],
            public_key="U3RhaW5sZXNzIHJvY2tz",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interactions.with_raw_response.signup(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interactions.with_streaming_response.signup(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(RunnerInteractionSignupResponse, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_status(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interactions.update_status(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interactions.update_status(
            body={
                "additionalInfo": [{}, {}, {}],
                "degredationMessage": "degredationMessage",
                "logUrl": "https://example.com",
                "region": "region",
                "runnerId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "systemDetails": "systemDetails",
                "version": "version",
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interactions.with_raw_response.update_status(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interactions.with_streaming_response.update_status(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True
