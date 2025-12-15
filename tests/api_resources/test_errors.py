# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestErrors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_errors(self, client: Gitpod) -> None:
        error = client.errors.report_errors()
        assert_matches_type(object, error, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_errors_with_all_params(self, client: Gitpod) -> None:
        error = client.errors.report_errors(
            events=[
                {
                    "breadcrumbs": [
                        {
                            "category": "category",
                            "data": {"foo": "string"},
                            "level": "ERROR_LEVEL_UNSPECIFIED",
                            "message": "message",
                            "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "environment": "environment",
                    "event_id": "210b9798eb53baa4e69d31c1071cf03d",
                    "exceptions": [
                        {
                            "mechanism": {
                                "data": {"foo": "string"},
                                "description": "description",
                                "handled": True,
                                "synthetic": True,
                                "type": "x",
                            },
                            "module": "module",
                            "stacktrace": [
                                {
                                    "colno": 0,
                                    "context_line": "contextLine",
                                    "filename": "filename",
                                    "function": "function",
                                    "in_app": True,
                                    "lineno": 0,
                                    "module": "module",
                                    "post_context": ["string"],
                                    "pre_context": ["string"],
                                    "vars": {"foo": "string"},
                                }
                            ],
                            "thread_id": "threadId",
                            "type": "x",
                            "value": "value",
                        }
                    ],
                    "extra": {"foo": "string"},
                    "fingerprint": ["x"],
                    "identity_id": "ecc2efdd-ddfa-31a9-c6f1-b833d337aa7c",
                    "level": "ERROR_LEVEL_UNSPECIFIED",
                    "logger": "logger",
                    "modules": {"foo": "string"},
                    "platform": "x",
                    "release": "release",
                    "request": {
                        "data": "data",
                        "headers": {"foo": "string"},
                        "method": "method",
                        "query_string": {"foo": "string"},
                        "url": "url",
                    },
                    "sdk": {"foo": "string"},
                    "server_name": "serverName",
                    "tags": {"foo": "string"},
                    "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "transaction": "transaction",
                }
            ],
        )
        assert_matches_type(object, error, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_errors(self, client: Gitpod) -> None:
        response = client.errors.with_raw_response.report_errors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        error = response.parse()
        assert_matches_type(object, error, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_errors(self, client: Gitpod) -> None:
        with client.errors.with_streaming_response.report_errors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            error = response.parse()
            assert_matches_type(object, error, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncErrors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_errors(self, async_client: AsyncGitpod) -> None:
        error = await async_client.errors.report_errors()
        assert_matches_type(object, error, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_errors_with_all_params(self, async_client: AsyncGitpod) -> None:
        error = await async_client.errors.report_errors(
            events=[
                {
                    "breadcrumbs": [
                        {
                            "category": "category",
                            "data": {"foo": "string"},
                            "level": "ERROR_LEVEL_UNSPECIFIED",
                            "message": "message",
                            "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "type": "type",
                        }
                    ],
                    "environment": "environment",
                    "event_id": "210b9798eb53baa4e69d31c1071cf03d",
                    "exceptions": [
                        {
                            "mechanism": {
                                "data": {"foo": "string"},
                                "description": "description",
                                "handled": True,
                                "synthetic": True,
                                "type": "x",
                            },
                            "module": "module",
                            "stacktrace": [
                                {
                                    "colno": 0,
                                    "context_line": "contextLine",
                                    "filename": "filename",
                                    "function": "function",
                                    "in_app": True,
                                    "lineno": 0,
                                    "module": "module",
                                    "post_context": ["string"],
                                    "pre_context": ["string"],
                                    "vars": {"foo": "string"},
                                }
                            ],
                            "thread_id": "threadId",
                            "type": "x",
                            "value": "value",
                        }
                    ],
                    "extra": {"foo": "string"},
                    "fingerprint": ["x"],
                    "identity_id": "ecc2efdd-ddfa-31a9-c6f1-b833d337aa7c",
                    "level": "ERROR_LEVEL_UNSPECIFIED",
                    "logger": "logger",
                    "modules": {"foo": "string"},
                    "platform": "x",
                    "release": "release",
                    "request": {
                        "data": "data",
                        "headers": {"foo": "string"},
                        "method": "method",
                        "query_string": {"foo": "string"},
                        "url": "url",
                    },
                    "sdk": {"foo": "string"},
                    "server_name": "serverName",
                    "tags": {"foo": "string"},
                    "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "transaction": "transaction",
                }
            ],
        )
        assert_matches_type(object, error, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_errors(self, async_client: AsyncGitpod) -> None:
        response = await async_client.errors.with_raw_response.report_errors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        error = await response.parse()
        assert_matches_type(object, error, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_errors(self, async_client: AsyncGitpod) -> None:
        async with async_client.errors.with_streaming_response.report_errors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            error = await response.parse()
            assert_matches_type(object, error, path=["response"])

        assert cast(Any, response.is_closed) is True
