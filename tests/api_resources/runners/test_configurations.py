# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.runners import ConfigurationValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate(self, client: Gitpod) -> None:
        configuration = client.runners.configurations.validate()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: Gitpod) -> None:
        configuration = client.runners.configurations.validate(
            environment_class={
                "id": "id",
                "runner_id": "runnerId",
                "configuration": [
                    {
                        "key": "key",
                        "value": "value",
                    }
                ],
                "description": "xxx",
                "display_name": "xxx",
                "enabled": True,
            },
            runner_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            scm_integration={
                "id": "integration-id",
                "host": "github.com",
                "issuer_url": "issuerUrl",
                "oauth_client_id": "client_id",
                "oauth_encrypted_client_secret": "U3RhaW5sZXNzIHJvY2tz",
                "oauth_plaintext_client_secret": "client_secret",
                "pat": True,
                "scm_id": "github",
                "virtual_directory": "virtualDirectory",
            },
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Gitpod) -> None:
        response = client.runners.configurations.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: Gitpod) -> None:
        with client.runners.configurations.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncGitpod) -> None:
        configuration = await async_client.runners.configurations.validate()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncGitpod) -> None:
        configuration = await async_client.runners.configurations.validate(
            environment_class={
                "id": "id",
                "runner_id": "runnerId",
                "configuration": [
                    {
                        "key": "key",
                        "value": "value",
                    }
                ],
                "description": "xxx",
                "display_name": "xxx",
                "enabled": True,
            },
            runner_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            scm_integration={
                "id": "integration-id",
                "host": "github.com",
                "issuer_url": "issuerUrl",
                "oauth_client_id": "client_id",
                "oauth_encrypted_client_secret": "U3RhaW5sZXNzIHJvY2tz",
                "oauth_plaintext_client_secret": "client_secret",
                "pat": True,
                "scm_id": "github",
                "virtual_directory": "virtualDirectory",
            },
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
