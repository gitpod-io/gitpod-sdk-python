import sys
from urllib.parse import urlparse

import gitpod
import gitpod.lib as util
from gitpod import AsyncGitpod
from gitpod.types.runner_check_authentication_for_host_response import SupportsPat


async def handle_pat_auth(client: AsyncGitpod, user_id: str, runner_id: str, host: str, supports_pat: SupportsPat) -> None:
    print("\nTo create a Personal Access Token:")
    create_url = supports_pat.create_url
    
    if create_url: 
        print(f"1. Visit: {create_url}")
    else:
        print(f"1. Go to {host} > Settings > Developer Settings")
    
    if supports_pat.required_scopes and len(supports_pat.required_scopes) > 0:
        required_scopes = ", ".join(supports_pat.required_scopes)
        print(f"2. Create a new token with the following scopes: {required_scopes}")
    else:
        print(f"2. Create a new token")
    
    if supports_pat.example:
        print(f"3. Copy the generated token (example: {supports_pat.example})")
    else:
        print(f"3. Copy the generated token")
    
    if supports_pat.docs_url:
        print(f"\nFor detailed instructions, visit: {supports_pat.docs_url}")

    pat = input("\nEnter your Personal Access Token: ").strip()
    if not pat:
        return

    await util.set_scm_pat(client, user_id, runner_id, host, pat)

async def verify_context_url(client: AsyncGitpod, context_url: str, runner_id: str) -> None:
    """Verify and handle authentication for a repository context URL.
    
    This function checks if the user has access to the specified repository and manages
    the authentication process if needed. Git access to the repository is required for
    environments to function properly.

    As an alternative, you can authenticate once via the Gitpod dashboard:
    1. Start a new environment 
    2. Complete the browser-based authentication flow
    
    See https://www.gitpod.io/docs/flex/source-control for more details.
    """
    host = urlparse(context_url).hostname
    if host is None:
        print("Error: Invalid context URL")
        sys.exit(1)

    user = (await client.users.get_authenticated_user()).user

    # Main authentication loop
    first_attempt = True
    while True:
        try:
            # Try to access the context URL
            await client.runners.parse_context_url(context_url=context_url, runner_id=runner_id)
            print("\n✓ Authentication verified successfully")
            return

        except gitpod.APIError as e:
            if e.code != "failed_precondition":
                raise e
            
        # Show authentication required message only on first attempt
        if first_attempt:
            print(f"\nAuthentication required for {host}")
            first_attempt = False

        # Get authentication options for the host
        auth_resp = await client.runners.check_authentication_for_host(
            host=host,
            runner_id=runner_id
        )

        # Handle re-authentication case
        if auth_resp.authenticated and not first_attempt:
            print("\nIt looks like you are already authenticated.")
            if input("Would you like to re-authenticate? (y/n): ").lower().strip() != 'y':
                print("\nAuthentication cancelled")
                sys.exit(1)
            else:
                print("\nRetrying authentication...")
                continue
                
        auth_methods: list[tuple[str, str]] = []
        if auth_resp.supports_oauth2:
            auth_methods.append(("OAuth", "Recommended"))
        if auth_resp.supports_pat:
            auth_methods.append(("Personal Access Token (PAT)", ""))

        if not auth_methods:
            print(f"\nError: No authentication method available for {host}")
            sys.exit(1)

        # Present authentication options
        if len(auth_methods) > 1:
            print("\nAvailable authentication methods:")
            for i, (method, note) in enumerate(auth_methods, 1):
                note_text = f" ({note})" if note else ""
                print(f"{i}. {method}{note_text}")
            
            choice = input(f"\nChoose authentication method (1-{len(auth_methods)}): ").strip()
            try:
                method_index = int(choice) - 1
                if not 0 <= method_index < len(auth_methods):
                    raise ValueError()
            except ValueError:
                method_index = 0  # Default to OAuth if invalid input
        else:
            method_index = 0

        # Handle chosen authentication method
        chosen_method = auth_methods[method_index][0]
        if chosen_method == "Personal Access Token (PAT)":
            assert auth_resp.supports_pat
            await handle_pat_auth(client, user.id, runner_id, host, auth_resp.supports_pat)
        else:
            assert auth_resp.supports_oauth2
            print(f"\nPlease visit the following URL to authenticate:")
            print(f"{auth_resp.supports_oauth2.auth_url}")
            if auth_resp.supports_oauth2.docs_url:
                print(f"\nFor detailed instructions, visit: {auth_resp.supports_oauth2.docs_url}")
            print("\nWaiting for authentication to complete...")
            input("Press Enter after completing authentication in your browser...") 