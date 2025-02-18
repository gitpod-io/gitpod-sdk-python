# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod._utils import parse_datetime
from gitpod.pagination import SyncServicesPage, AsyncServicesPage
from gitpod.types.environments.automations import (
    Service,
    ServiceCreateResponse,
    ServiceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        service = client.environments.automations.services.create()
        assert_matches_type(ServiceCreateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.create(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            metadata={
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "creator": {
                    "id": "id",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                },
                "description": "Runs the development web server",
                "name": "Web Server",
                "reference": "web-server",
                "triggered_by": [
                    {
                        "manual": True,
                        "post_devcontainer_start": True,
                        "post_environment_start": True,
                    }
                ],
            },
            spec={
                "commands": {
                    "ready": "curl -s http://localhost:3000",
                    "start": "npm run dev",
                    "stop": "stop",
                },
                "desired_phase": "SERVICE_PHASE_UNSPECIFIED",
                "runs_on": {
                    "docker": {
                        "environment": ["string"],
                        "image": "x",
                    }
                },
                "session": "session",
                "spec_version": "specVersion",
            },
        )
        assert_matches_type(ServiceCreateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceCreateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceCreateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        service = client.environments.automations.services.retrieve()
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        service = client.environments.automations.services.update()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.update(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            metadata={
                "description": "description",
                "name": "x",
                "triggered_by": {
                    "trigger": [
                        {
                            "manual": True,
                            "post_devcontainer_start": True,
                            "post_environment_start": True,
                        }
                    ]
                },
            },
            spec={
                "commands": {
                    "ready": "curl -s http://localhost:8080",
                    "start": "npm run start:dev",
                    "stop": "stop",
                },
                "runs_on": {
                    "docker": {
                        "environment": ["string"],
                        "image": "x",
                    }
                },
            },
            status={
                "failure_message": "failureMessage",
                "log_url": "logUrl",
                "phase": "SERVICE_PHASE_UNSPECIFIED",
                "session": "session",
            },
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        service = client.environments.automations.services.list()
        assert_matches_type(SyncServicesPage[Service], service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.list(
            token="token",
            page_size=0,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "references": ["web-server", "database"],
                "service_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncServicesPage[Service], service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(SyncServicesPage[Service], service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(SyncServicesPage[Service], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        service = client.environments.automations.services.delete()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.delete(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            force=False,
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_start(self, client: Gitpod) -> None:
        service = client.environments.automations.services.start()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_start_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.start(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_start(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_start(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        service = client.environments.automations.services.stop()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        service = client.environments.automations.services.stop(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environments.automations.services.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environments.automations.services.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.create()
        assert_matches_type(ServiceCreateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.create(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            metadata={
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "creator": {
                    "id": "id",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                },
                "description": "Runs the development web server",
                "name": "Web Server",
                "reference": "web-server",
                "triggered_by": [
                    {
                        "manual": True,
                        "post_devcontainer_start": True,
                        "post_environment_start": True,
                    }
                ],
            },
            spec={
                "commands": {
                    "ready": "curl -s http://localhost:3000",
                    "start": "npm run dev",
                    "stop": "stop",
                },
                "desired_phase": "SERVICE_PHASE_UNSPECIFIED",
                "runs_on": {
                    "docker": {
                        "environment": ["string"],
                        "image": "x",
                    }
                },
                "session": "session",
                "spec_version": "specVersion",
            },
        )
        assert_matches_type(ServiceCreateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceCreateResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceCreateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.retrieve()
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceRetrieveResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.update()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.update(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            metadata={
                "description": "description",
                "name": "x",
                "triggered_by": {
                    "trigger": [
                        {
                            "manual": True,
                            "post_devcontainer_start": True,
                            "post_environment_start": True,
                        }
                    ]
                },
            },
            spec={
                "commands": {
                    "ready": "curl -s http://localhost:8080",
                    "start": "npm run start:dev",
                    "stop": "stop",
                },
                "runs_on": {
                    "docker": {
                        "environment": ["string"],
                        "image": "x",
                    }
                },
            },
            status={
                "failure_message": "failureMessage",
                "log_url": "logUrl",
                "phase": "SERVICE_PHASE_UNSPECIFIED",
                "session": "session",
            },
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.list()
        assert_matches_type(AsyncServicesPage[Service], service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.list(
            token="token",
            page_size=0,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "references": ["web-server", "database"],
                "service_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncServicesPage[Service], service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(AsyncServicesPage[Service], service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(AsyncServicesPage[Service], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.delete()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.delete(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            force=False,
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_start(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.start()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.start(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.stop()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.environments.automations.services.stop(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.services.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.services.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True
