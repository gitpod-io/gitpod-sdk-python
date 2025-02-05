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

    @pytest.mark.skip()
    @parametrize
    def test_method_validate_overload_1(self, client: Gitpod) -> None:
        configuration = client.runners.configurations.validate(
            environment_class={},
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_validate_with_all_params_overload_1(self, client: Gitpod) -> None:
        configuration = client.runners.configurations.validate(
            environment_class={
                "id": "id",
                "configuration": [
                    {
                        "key": "key",
                        "value": "value",
                    }
                ],
                "description": "xxx",
                "display_name": "xxx",
                "enabled": True,
                "runner_id": "runnerId",
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate_overload_1(self, client: Gitpod) -> None:
        response = client.runners.configurations.with_raw_response.validate(
            environment_class={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate_overload_1(self, client: Gitpod) -> None:
        with client.runners.configurations.with_streaming_response.validate(
            environment_class={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_validate_overload_2(self, client: Gitpod) -> None:
        configuration = client.runners.configurations.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_validate_with_all_params_overload_2(self, client: Gitpod) -> None:
        configuration = client.runners.configurations.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate_overload_2(self, client: Gitpod) -> None:
        response = client.runners.configurations.with_raw_response.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate_overload_2(self, client: Gitpod) -> None:
        with client.runners.configurations.with_streaming_response.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate_overload_1(self, async_client: AsyncGitpod) -> None:
        configuration = await async_client.runners.configurations.validate(
            environment_class={},
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        configuration = await async_client.runners.configurations.validate(
            environment_class={
                "id": "id",
                "configuration": [
                    {
                        "key": "key",
                        "value": "value",
                    }
                ],
                "description": "xxx",
                "display_name": "xxx",
                "enabled": True,
                "runner_id": "runnerId",
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.with_raw_response.validate(
            environment_class={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.with_streaming_response.validate(
            environment_class={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate_overload_2(self, async_client: AsyncGitpod) -> None:
        configuration = await async_client.runners.configurations.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate_with_all_params_overload_2(self, async_client: AsyncGitpod) -> None:
        configuration = await async_client.runners.configurations.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.with_raw_response.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.with_streaming_response.validate(
            scm_integration={"oauth_client_id": "oauthClientId"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationValidateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
