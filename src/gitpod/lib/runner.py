from gitpod._client import AsyncGitpod


async def set_scm_pat(client: AsyncGitpod, user_id: str, runner_id: str, host: str, pat: str) -> None:
    """Set a Personal Access Token (PAT) for source control authentication.

    This will delete any existing tokens for the given host and create a new one.

    Args:
        client: The AsyncGitpod client instance
        user_id: ID of the user to set the token for
        runner_id: ID of the runner to associate the token with
        host: Source control host (e.g. github.com, gitlab.com)
        pat: The Personal Access Token string
    """
    tokens_response = await client.runners.configurations.host_authentication_tokens.list(
        filter={
            "user_id": user_id,
            "runner_id": runner_id,
        }
    )

    if tokens_response and tokens_response.tokens:
        for token in tokens_response.tokens:
            if token.host == host:
                await client.runners.configurations.host_authentication_tokens.delete(
                    id=token.id
                )

    await client.runners.configurations.host_authentication_tokens.create(
        token=pat,
        host=host,
        runner_id=runner_id,
        user_id=user_id,
        source="HOST_AUTHENTICATION_TOKEN_SOURCE_PAT"
    )