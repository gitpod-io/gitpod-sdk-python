# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.runner_configurations import (
    ConfigurationSchemaCreateResponse,
    ConfigurationSchemaRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurationSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        configuration_schema = client.runner_configurations.configuration_schema.create(
            connect_protocol_version=1,
        )
        assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        configuration_schema = client.runner_configurations.configuration_schema.create(
            connect_protocol_version=1,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runner_configurations.configuration_schema.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration_schema = response.parse()
        assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runner_configurations.configuration_schema.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration_schema = response.parse()
            assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        configuration_schema = client.runner_configurations.configuration_schema.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        configuration_schema = client.runner_configurations.configuration_schema.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runner_configurations.configuration_schema.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration_schema = response.parse()
        assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runner_configurations.configuration_schema.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration_schema = response.parse()
            assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigurationSchema:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        configuration_schema = await async_client.runner_configurations.configuration_schema.create(
            connect_protocol_version=1,
        )
        assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        configuration_schema = await async_client.runner_configurations.configuration_schema.create(
            connect_protocol_version=1,
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.configuration_schema.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration_schema = await response.parse()
        assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.configuration_schema.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration_schema = await response.parse()
            assert_matches_type(ConfigurationSchemaCreateResponse, configuration_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        configuration_schema = await async_client.runner_configurations.configuration_schema.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        configuration_schema = await async_client.runner_configurations.configuration_schema.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.configuration_schema.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration_schema = await response.parse()
        assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.configuration_schema.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration_schema = await response.parse()
            assert_matches_type(ConfigurationSchemaRetrieveResponse, configuration_schema, path=["response"])

        assert cast(Any, response.is_closed) is True
