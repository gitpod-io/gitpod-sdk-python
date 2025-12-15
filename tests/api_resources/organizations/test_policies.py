# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.organizations import PolicyRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        policy = client.organizations.policies.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(PolicyRetrieveResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.policies.with_raw_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyRetrieveResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.policies.with_streaming_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyRetrieveResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        policy = client.organizations.policies.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        policy = client.organizations.policies.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            agent_policy={
                "command_deny_list": ["string"],
                "mcp_disabled": True,
                "scm_tools_disabled": True,
            },
            allowed_editor_ids=["string"],
            allow_local_runners=True,
            default_editor_id="defaultEditorId",
            default_environment_image="defaultEnvironmentImage",
            delete_archived_environments_after="+9125115.360s",
            editor_version_restrictions={"foo": {"allowed_versions": ["string"]}},
            maximum_environment_lifetime="+9125115.360s",
            maximum_environments_per_user="20",
            maximum_environment_timeout="3600s",
            maximum_running_environments_per_user="5",
            members_create_projects=True,
            members_require_projects=True,
            port_sharing_disabled=True,
            require_custom_domain_access=True,
            security_agent_policy={
                "crowdstrike": {
                    "additional_options": {"foo": "string"},
                    "cid_secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enabled": True,
                    "image": "image",
                    "tags": "tags",
                }
            },
        )
        assert_matches_type(object, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.policies.with_raw_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(object, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.policies.with_streaming_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(object, policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        policy = await async_client.organizations.policies.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(PolicyRetrieveResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.policies.with_raw_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyRetrieveResponse, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.policies.with_streaming_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyRetrieveResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        policy = await async_client.organizations.policies.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        policy = await async_client.organizations.policies.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            agent_policy={
                "command_deny_list": ["string"],
                "mcp_disabled": True,
                "scm_tools_disabled": True,
            },
            allowed_editor_ids=["string"],
            allow_local_runners=True,
            default_editor_id="defaultEditorId",
            default_environment_image="defaultEnvironmentImage",
            delete_archived_environments_after="+9125115.360s",
            editor_version_restrictions={"foo": {"allowed_versions": ["string"]}},
            maximum_environment_lifetime="+9125115.360s",
            maximum_environments_per_user="20",
            maximum_environment_timeout="3600s",
            maximum_running_environments_per_user="5",
            members_create_projects=True,
            members_require_projects=True,
            port_sharing_disabled=True,
            require_custom_domain_access=True,
            security_agent_policy={
                "crowdstrike": {
                    "additional_options": {"foo": "string"},
                    "cid_secret_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "enabled": True,
                    "image": "image",
                    "tags": "tags",
                }
            },
        )
        assert_matches_type(object, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.policies.with_raw_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(object, policy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.policies.with_streaming_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(object, policy, path=["response"])

        assert cast(Any, response.is_closed) is True
