# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    SecurityPolicy,
    SecurityPolicyCreateResponse,
    SecurityPolicyUpdateResponse,
    SecurityPolicyRetrieveResponse,
)
from gitpod.pagination import SyncSecurityPoliciesPage, AsyncSecurityPoliciesPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecurityPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        security_policy = client.security_policies.create(
            metadata={},
            spec={},
        )
        assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        security_policy = client.security_policies.create(
            metadata={"name": "Veto Exec audit-first"},
            spec={
                "executables": {
                    "default_effect": "EFFECT_ALLOW",
                    "rules": [
                        {
                            "effect": "EFFECT_AUDIT",
                            "path": "npx",
                        },
                        {
                            "effect": "EFFECT_BLOCK",
                            "path": "/usr/bin/curl",
                        },
                    ],
                }
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.security_policies.with_raw_response.create(
            metadata={},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = response.parse()
        assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.security_policies.with_streaming_response.create(
            metadata={},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = response.parse()
            assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        security_policy = client.security_policies.retrieve()
        assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        security_policy = client.security_policies.retrieve(
            security_policy_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.security_policies.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = response.parse()
        assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.security_policies.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = response.parse()
            assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        security_policy = client.security_policies.update()
        assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        security_policy = client.security_policies.update(
            metadata={"name": "x"},
            security_policy_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            spec={
                "executables": {
                    "default_effect": "EFFECT_ALLOW",
                    "rules": [
                        {
                            "effect": "EFFECT_BLOCK",
                            "path": "npx",
                        },
                        {
                            "effect": "EFFECT_BLOCK",
                            "path": "/usr/bin/curl",
                        },
                    ],
                }
            },
        )
        assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.security_policies.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = response.parse()
        assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.security_policies.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = response.parse()
            assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        security_policy = client.security_policies.list()
        assert_matches_type(SyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        security_policy = client.security_policies.list(
            token="token",
            page_size=0,
            filter={
                "organization_id": "b0e12f6c-4c67-429d-a4a6-d9838b5da047",
                "search": "search",
                "security_policy_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.security_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = response.parse()
        assert_matches_type(SyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.security_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = response.parse()
            assert_matches_type(SyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        security_policy = client.security_policies.delete()
        assert_matches_type(object, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        security_policy = client.security_policies.delete(
            security_policy_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.security_policies.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = response.parse()
        assert_matches_type(object, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.security_policies.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = response.parse()
            assert_matches_type(object, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecurityPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.create(
            metadata={},
            spec={},
        )
        assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.create(
            metadata={"name": "Veto Exec audit-first"},
            spec={
                "executables": {
                    "default_effect": "EFFECT_ALLOW",
                    "rules": [
                        {
                            "effect": "EFFECT_AUDIT",
                            "path": "npx",
                        },
                        {
                            "effect": "EFFECT_BLOCK",
                            "path": "/usr/bin/curl",
                        },
                    ],
                }
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.security_policies.with_raw_response.create(
            metadata={},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = await response.parse()
        assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.security_policies.with_streaming_response.create(
            metadata={},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = await response.parse()
            assert_matches_type(SecurityPolicyCreateResponse, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.retrieve()
        assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.retrieve(
            security_policy_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.security_policies.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = await response.parse()
        assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.security_policies.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = await response.parse()
            assert_matches_type(SecurityPolicyRetrieveResponse, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.update()
        assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.update(
            metadata={"name": "x"},
            security_policy_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            spec={
                "executables": {
                    "default_effect": "EFFECT_ALLOW",
                    "rules": [
                        {
                            "effect": "EFFECT_BLOCK",
                            "path": "npx",
                        },
                        {
                            "effect": "EFFECT_BLOCK",
                            "path": "/usr/bin/curl",
                        },
                    ],
                }
            },
        )
        assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.security_policies.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = await response.parse()
        assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.security_policies.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = await response.parse()
            assert_matches_type(SecurityPolicyUpdateResponse, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.list()
        assert_matches_type(AsyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.list(
            token="token",
            page_size=0,
            filter={
                "organization_id": "b0e12f6c-4c67-429d-a4a6-d9838b5da047",
                "search": "search",
                "security_policy_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.security_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = await response.parse()
        assert_matches_type(AsyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.security_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = await response.parse()
            assert_matches_type(AsyncSecurityPoliciesPage[SecurityPolicy], security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.delete()
        assert_matches_type(object, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        security_policy = await async_client.security_policies.delete(
            security_policy_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.security_policies.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_policy = await response.parse()
        assert_matches_type(object, security_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.security_policies.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_policy = await response.parse()
            assert_matches_type(object, security_policy, path=["response"])

        assert cast(Any, response.is_closed) is True
