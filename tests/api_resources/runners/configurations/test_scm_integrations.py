# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncPersonalAccessTokensPage, AsyncPersonalAccessTokensPage
from gitpod.types.runners.configurations import (
    ScmIntegrationListResponse,
    ScmIntegrationCreateResponse,
    ScmIntegrationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScmIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.create(
            oauth_client_id="oauthClientId",
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.create(
            oauth_client_id="oauthClientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.create(
            oauth_client_id="oauthClientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.create(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.create(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.create(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.retrieve()
        assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.update(
            oauth_client_id="oauthClientId",
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.update(
            oauth_client_id="oauthClientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.update(
            oauth_client_id="oauthClientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_2(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.update(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.update(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.update(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_3(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.update(
            pat=True,
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.update(
            pat=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.update(
            pat=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.list()
        assert_matches_type(
            SyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.list(
            token="token",
            page_size=0,
            filter={"runner_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(
            SyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(
            SyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(
                SyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.delete()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        scm_integration = client.runners.configurations.scm_integrations.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.runners.configurations.scm_integrations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.runners.configurations.scm_integrations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScmIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.create(
            oauth_client_id="oauthClientId",
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.create(
            oauth_client_id="oauthClientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.create(
            oauth_client_id="oauthClientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.create(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.create(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.create(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(ScmIntegrationCreateResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.retrieve()
        assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(ScmIntegrationRetrieveResponse, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.update(
            oauth_client_id="oauthClientId",
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.update(
            oauth_client_id="oauthClientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.update(
            oauth_client_id="oauthClientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.update(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.update(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.update(
            oauth_plaintext_client_secret="oauthPlaintextClientSecret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.update(
            pat=True,
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.update(
            pat=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.update(
            pat=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.list()
        assert_matches_type(
            AsyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.list(
            token="token",
            page_size=0,
            filter={"runner_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(
            AsyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(
            AsyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(
                AsyncPersonalAccessTokensPage[ScmIntegrationListResponse], scm_integration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.delete()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        scm_integration = await async_client.runners.configurations.scm_integrations.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.scm_integrations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scm_integration = await response.parse()
        assert_matches_type(object, scm_integration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.scm_integrations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scm_integration = await response.parse()
            assert_matches_type(object, scm_integration, path=["response"])

        assert cast(Any, response.is_closed) is True
