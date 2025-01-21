# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.runner_configurations import ScmIntegrationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScmIntegration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        scm_integration = client.runner_configurations.scm_integration.create(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        scm_integration = client.runner_configurations.scm_integration.create(
            body={
                "host": "host",
                "pat": True,
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runner_configurations.scm_integration.with_raw_response.create(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runner_configurations.scm_integration.with_streaming_response.create(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScmIntegration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runner_configurations.scm_integration.create(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runner_configurations.scm_integration.create(
            body={
                "host": "host",
                "pat": True,
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.scm_integration.with_raw_response.create(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.scm_integration.with_streaming_response.create(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True
