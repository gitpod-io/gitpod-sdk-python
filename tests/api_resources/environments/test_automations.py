# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.environments import AutomationUpsertResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upsert(self, client: Gitpod) -> None:
        automation = client.environments.automations.upsert()
        assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upsert_with_all_params(self, client: Gitpod) -> None:
        automation = client.environments.automations.upsert(
            automations_file={
                "services": {
                    "foo": {
                        "commands": {
                            "ready": "ready",
                            "start": "x",
                            "stop": "stop",
                        },
                        "description": "description",
                        "name": "x",
                        "runs_on": {
                            "docker": {
                                "environment": ["string"],
                                "image": "x",
                            }
                        },
                        "triggered_by": ["manual"],
                    }
                },
                "tasks": {
                    "foo": {
                        "command": "x",
                        "depends_on": ["string"],
                        "description": "description",
                        "name": "x",
                        "runs_on": {
                            "docker": {
                                "environment": ["string"],
                                "image": "x",
                            }
                        },
                        "triggered_by": ["manual"],
                    }
                },
            },
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upsert(self, client: Gitpod) -> None:
        response = client.environments.automations.with_raw_response.upsert()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upsert(self, client: Gitpod) -> None:
        with client.environments.automations.with_streaming_response.upsert() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutomations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upsert(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.environments.automations.upsert()
        assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.environments.automations.upsert(
            automations_file={
                "services": {
                    "foo": {
                        "commands": {
                            "ready": "ready",
                            "start": "x",
                            "stop": "stop",
                        },
                        "description": "description",
                        "name": "x",
                        "runs_on": {
                            "docker": {
                                "environment": ["string"],
                                "image": "x",
                            }
                        },
                        "triggered_by": ["manual"],
                    }
                },
                "tasks": {
                    "foo": {
                        "command": "x",
                        "depends_on": ["string"],
                        "description": "description",
                        "name": "x",
                        "runs_on": {
                            "docker": {
                                "environment": ["string"],
                                "image": "x",
                            }
                        },
                        "triggered_by": ["manual"],
                    }
                },
            },
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.with_raw_response.upsert()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.with_streaming_response.upsert() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationUpsertResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True
