# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    SecretListResponse,
    SecretCreateResponse,
    SecretGetValueResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            environment_variable=True,
            connect_protocol_version=1,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            environment_variable=True,
            connect_protocol_version=1,
            file_path="filePath",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.create(
            environment_variable=True,
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.create(
            environment_variable=True,
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            file_path="filePath",
            connect_protocol_version=1,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            file_path="filePath",
            connect_protocol_version=1,
            environment_variable=True,
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.create(
            file_path="filePath",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.create(
            file_path="filePath",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            connect_protocol_version=1,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            connect_protocol_version=1,
            environment_variable=True,
            file_path="filePath",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        secret = client.secrets.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        secret = client.secrets.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.delete(
            connect_protocol_version=1,
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_value(self, client: Gitpod) -> None:
        secret = client.secrets.get_value(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @parametrize
    def test_method_get_value_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.get_value(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_get_value(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.get_value(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_get_value(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.get_value(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretGetValueResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_value(self, client: Gitpod) -> None:
        secret = client.secrets.update_value(
            connect_protocol_version=1,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    def test_method_update_value_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.update_value(
            connect_protocol_version=1,
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    def test_raw_response_update_value(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.update_value(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    def test_streaming_response_update_value(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.update_value(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            environment_variable=True,
            connect_protocol_version=1,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            environment_variable=True,
            connect_protocol_version=1,
            file_path="filePath",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.create(
            environment_variable=True,
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.create(
            environment_variable=True,
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            file_path="filePath",
            connect_protocol_version=1,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            file_path="filePath",
            connect_protocol_version=1,
            environment_variable=True,
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.create(
            file_path="filePath",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.create(
            file_path="filePath",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            connect_protocol_version=1,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            connect_protocol_version=1,
            environment_variable=True,
            file_path="filePath",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.delete(
            connect_protocol_version=1,
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_value(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.get_value(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @parametrize
    async def test_method_get_value_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.get_value(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_get_value(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.get_value(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_get_value(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.get_value(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretGetValueResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_value(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.update_value(
            connect_protocol_version=1,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    async def test_method_update_value_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.update_value(
            connect_protocol_version=1,
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    async def test_raw_response_update_value(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.update_value(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @parametrize
    async def test_streaming_response_update_value(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.update_value(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True
