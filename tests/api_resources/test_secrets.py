# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Secret,
    SecretCreateResponse,
    SecretGetValueResponse,
)
from gitpod.pagination import SyncSecretsPage, AsyncSecretsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        secret = client.secrets.create()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.create(
            container_registry_basic_auth_host="https://example.com",
            environment_variable=True,
            file_path="filePath",
            name="DATABASE_URL",
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            value="postgresql://user:pass@localhost:5432/db",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        secret = client.secrets.list()
        assert_matches_type(SyncSecretsPage[Secret], secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.list(
            token="token",
            page_size=0,
            filter={"project_ids": ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"]},
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncSecretsPage[Secret], secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncSecretsPage[Secret], secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncSecretsPage[Secret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        secret = client.secrets.delete()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.delete(
            secret_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_value(self, client: Gitpod) -> None:
        secret = client.secrets.get_value()
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_value_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.get_value(
            secret_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_value(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.get_value()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_value(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.get_value() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretGetValueResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_value(self, client: Gitpod) -> None:
        secret = client.secrets.update_value()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_value_with_all_params(self, client: Gitpod) -> None:
        secret = client.secrets.update_value(
            secret_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            value="new-secret-value",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_value(self, client: Gitpod) -> None:
        response = client.secrets.with_raw_response.update_value()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_value(self, client: Gitpod) -> None:
        with client.secrets.with_streaming_response.update_value() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.create(
            container_registry_basic_auth_host="https://example.com",
            environment_variable=True,
            file_path="filePath",
            name="DATABASE_URL",
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            value="postgresql://user:pass@localhost:5432/db",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.list()
        assert_matches_type(AsyncSecretsPage[Secret], secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.list(
            token="token",
            page_size=0,
            filter={"project_ids": ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"]},
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncSecretsPage[Secret], secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncSecretsPage[Secret], secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncSecretsPage[Secret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.delete()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.delete(
            secret_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_value(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.get_value()
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_value_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.get_value(
            secret_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_value(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.get_value()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretGetValueResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_value(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.get_value() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretGetValueResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_value(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.update_value()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_value_with_all_params(self, async_client: AsyncGitpod) -> None:
        secret = await async_client.secrets.update_value(
            secret_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            value="new-secret-value",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_value(self, async_client: AsyncGitpod) -> None:
        response = await async_client.secrets.with_raw_response.update_value()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_value(self, async_client: AsyncGitpod) -> None:
        async with async_client.secrets.with_streaming_response.update_value() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True
