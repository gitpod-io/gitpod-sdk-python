# Changelog

## 0.11.0 (2026-04-02)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.10.0...v0.11.0)

### Features

* [backend/api] add backend search for group members ([0eb24b8](https://github.com/gitpod-io/gitpod-sdk-python/commit/0eb24b80e8a7b32ad08fbdd6e40fc3862b6545dc))
* **api:** add acknowledge_token param to environments.start method ([19ce45f](https://github.com/gitpod-io/gitpod-sdk-python/commit/19ce45ff07385a58858da61619c35291b4bd93aa))
* **api:** add agent_message parameter to agents.send_to_execution ([f7b21f6](https://github.com/gitpod-io/gitpod-sdk-python/commit/f7b21f6d4b9c54a12e4820b4a8226b751af0e7da))
* **api:** add automations resource with workflows/executions/actions ([7cdce62](https://github.com/gitpod-io/gitpod-sdk-python/commit/7cdce62ead18e8383b8e6119e08361a62d9b653e))
* **api:** add bpf_debug_level field to KernelControlsConfig ([d0cf7a4](https://github.com/gitpod-io/gitpod-sdk-python/commit/d0cf7a47fc5e68b96a40152ba8f26476da9ded02))
* **api:** add claims_expression parameter to sso_configurations create and update ([d484eb4](https://github.com/gitpod-io/gitpod-sdk-python/commit/d484eb4c984711813f1adc0558c43e27eb1b05f0))
* **api:** add conversation_sharing_policy field to agent_policy ([9b72125](https://github.com/gitpod-io/gitpod-sdk-python/commit/9b721252171aef850f1bb94db07aa5891d58429f))
* **api:** add credential_proxy field to environment_spec Secret ([d8b5e78](https://github.com/gitpod-io/gitpod-sdk-python/commit/d8b5e78f0edc26a0548c701d73a07a349bc01423))
* **api:** add custom security agents to organizations policies ([dd01263](https://github.com/gitpod-io/gitpod-sdk-python/commit/dd012637ab566c8fffc871f131dada3543ed63ac))
* **api:** add desired_size field to WarmPoolStatus ([3c0ca3c](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c0ca3c63cd9057f721011ecb5d052e2f7661666))
* **api:** add disabled parameter to automations update method ([79b5f69](https://github.com/gitpod-io/gitpod-sdk-python/commit/79b5f6953e39db8117c22f295fe936d8d75a8963))
* **api:** add environment field to WakeEventParam ([ff7eab3](https://github.com/gitpod-io/gitpod-sdk-python/commit/ff7eab324a5c44025a30a4379124577d1a28d972))
* **api:** add exclude_prompt_content parameter to agents list_prompts method ([1b78cec](https://github.com/gitpod-io/gitpod-sdk-python/commit/1b78cecf7a623ad29c4d5cdfc8fe3a04a8d024c7))
* **api:** add exclude_team_ids parameter to organization list members ([9e0a178](https://github.com/gitpod-io/gitpod-sdk-python/commit/9e0a17869e19e07581e7d4ca132e7f650951ced0))
* **api:** add filter parameter to groups list method ([c21fcff](https://github.com/gitpod-io/gitpod-sdk-python/commit/c21fcff4e84363a6c73d54516afea8ab40c8f218))
* **api:** add has_failed_execution_since filter parameter to automation list method ([1f306a1](https://github.com/gitpod-io/gitpod-sdk-python/commit/1f306a1429270a2697706e8c83e415da2d5d24c4))
* **api:** add lockdown_at field to environment status ([6317ac9](https://github.com/gitpod-io/gitpod-sdk-python/commit/6317ac97e4de079d158a0839eea63b8b4f11825f))
* **api:** add loop_conditions to agent execution, loop_retrigger to wake event, make timer optional ([e67d5fe](https://github.com/gitpod-io/gitpod-sdk-python/commit/e67d5fe4134e45109e6430d546c27fe5a2bcb51b))
* **api:** add managed_metrics_enabled field to metrics configuration ([b390afb](https://github.com/gitpod-io/gitpod-sdk-python/commit/b390afb75f2500b05b9f43c3c4a2bf41738365a5))
* **api:** add max_subagents_per_environment field to organizations agent policy ([bce5c4d](https://github.com/gitpod-io/gitpod-sdk-python/commit/bce5c4d30e3ae15c463b2808647f81475a08c152))
* **api:** add min_size/max_size parameters to prebuilds warm pool methods ([aeba614](https://github.com/gitpod-io/gitpod-sdk-python/commit/aeba614dff3dcea43e05a803609f2a61fd4981f2))
* **api:** add notification resource type ([e5a82b6](https://github.com/gitpod-io/gitpod-sdk-python/commit/e5a82b65e794c60c223f1eaed16a3fcf54b8a8bc))
* **api:** add organization_tier field to identity get_authenticated_identity response ([fb627da](https://github.com/gitpod-io/gitpod-sdk-python/commit/fb627dad41802c02ae02ba1621968be8423dd726))
* **api:** add read_only field to PersonalAccessToken proto messages ([5b99de2](https://github.com/gitpod-io/gitpod-sdk-python/commit/5b99de2713301a27b6362837ca0acf2b63406188))
* **api:** add Report boolean/float/integer/string schema types ([467c68f](https://github.com/gitpod-io/gitpod-sdk-python/commit/467c68fbcfccf85ecbadb0cc9f845000687fcf86))
* **api:** add resource_ids to role assignments, restructure executable deny list in policies ([b30fc23](https://github.com/gitpod-io/gitpod-sdk-python/commit/b30fc2332c0d2f4c8267c00d15a2e0a3f43446ec))
* **api:** add RESOURCE_ROLE_AGENT_EXECUTION_VIEWER to ResourceRole enum ([88048fd](https://github.com/gitpod-io/gitpod-sdk-python/commit/88048fda6787010a8db49ff53d65a964ba576fb0))
* **api:** add RESOURCE_ROLE_ORG_AUDIT_LOG_READER to ResourceRole enum ([55549e9](https://github.com/gitpod-io/gitpod-sdk-python/commit/55549e977284c115c1b10b507d2a8865fac6a184))
* **api:** add resource_type_filters parameter to events watch method ([141bcd4](https://github.com/gitpod-io/gitpod-sdk-python/commit/141bcd4c6c1255dbb2ea37838ea87239efa62c81))
* **api:** add role and sender_execution_id fields to agent messages ([8cbc1ca](https://github.com/gitpod-io/gitpod-sdk-python/commit/8cbc1ca652eb9e2806555ca965d056f63c36dbd8))
* **api:** add RUNNER_CAPABILITY_ASG_WARM_POOL to RunnerCapability type ([28f6118](https://github.com/gitpod-io/gitpod-sdk-python/commit/28f6118559d32a814b5a76e30feaba36a5295a45))
* **api:** add RUNNER_CAPABILITY_WARM_POOL to runner_capability ([b058adf](https://github.com/gitpod-io/gitpod-sdk-python/commit/b058adf259789bb14f556f2c67b6f002fb654046))
* **api:** add search parameter to agent list prompts filter ([9b809fa](https://github.com/gitpod-io/gitpod-sdk-python/commit/9b809fae3ff472e26446e122e3347ebaf6111548))
* **api:** add SESSION_ADMIN and SESSION_USER roles to ResourceRole ([1fa7909](https://github.com/gitpod-io/gitpod-sdk-python/commit/1fa7909bd79fbd5f0d89724dd1ae14ac4ca79250))
* **api:** add session_id parameter to agents start_execution, environments create ([50cf2eb](https://github.com/gitpod-io/gitpod-sdk-python/commit/50cf2eb8b5a932328c7ded80332171ed28ca4e43))
* **api:** add session_id parameter to environments.create_from_project ([3c95ecc](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c95ecc227bdbdeeb4a401deb59a53e7a1c5034d))
* **api:** add session_ids filter to agents/environments list methods ([bbf9719](https://github.com/gitpod-io/gitpod-sdk-python/commit/bbf9719b7c47ed7cbe57211ef1da14e8b11aecc3))
* **api:** add snapshot_size_bytes field to PrebuildStatus ([c0764ca](https://github.com/gitpod-io/gitpod-sdk-python/commit/c0764ca0574ab440cad5fb732ca8076d11346e5e))
* **api:** add SONNET_4_6 model variants to agent_execution Status ([e87f54b](https://github.com/gitpod-io/gitpod-sdk-python/commit/e87f54b36e2913913125398b6e36223c795b9562))
* **api:** add sort option to ListAuditLogs ([19af3c6](https://github.com/gitpod-io/gitpod-sdk-python/commit/19af3c6ad9ba8ae3ca8605b26195fc27f8810d5f))
* **api:** add sort parameter to projects list, SortOrder/SortParam types ([fada768](https://github.com/gitpod-io/gitpod-sdk-python/commit/fada768b6dbe0721d4e6d93dca8ff2d6dc44f648))
* **api:** add SUPPORTED_MODEL_HAIKU_4_5 to agent_execution Status enum ([85c063b](https://github.com/gitpod-io/gitpod-sdk-python/commit/85c063b47e0cc8875f1b3c2a2d17c386fea76df4))
* **api:** add team admin and viewer roles to ResourceRole ([85b0437](https://github.com/gitpod-io/gitpod-sdk-python/commit/85b043796677897ef9ea8f5d92c129b515107890))
* **api:** add terminal field to RunsOn ([63ac31a](https://github.com/gitpod-io/gitpod-sdk-python/commit/63ac31aac183b0e174ef0d646ee8ccb8bf77f567))
* **api:** add time range filters to event list method ([c89b37e](https://github.com/gitpod-io/gitpod-sdk-python/commit/c89b37ec3240396215fba5b77b19c29ae598da2e))
* **api:** add update_window field to runner configuration ([97caa20](https://github.com/gitpod-io/gitpod-sdk-python/commit/97caa205330f086839652d16e76067d603058923))
* **api:** add wake_event parameter to agents send_to_execution method ([893e4b3](https://github.com/gitpod-io/gitpod-sdk-python/commit/893e4b37b75000dee0b99a0e82fe5c62a2732dd5))
* **api:** add warm pool methods to prebuilds ([68b693f](https://github.com/gitpod-io/gitpod-sdk-python/commit/68b693fe0134ac6df5aa06f7cc9409c15c9308a5))
* **api:** remove acknowledge_token parameter from environments.start ([340b6f2](https://github.com/gitpod-io/gitpod-sdk-python/commit/340b6f28ae6fa15ea3955d10720dcd44a6e85651))
* **backend/api,dashboard:** add server-side `recentlyCompleted` sort for `ListWorkflows` ([2d1ab67](https://github.com/gitpod-io/gitpod-sdk-python/commit/2d1ab675f63a20c402547a310de3cb77a19cb5a3))
* **internal:** implement indices array format for query and form serialization ([0829d27](https://github.com/gitpod-io/gitpod-sdk-python/commit/0829d27d4928a9affd3cefb0431cd176d40e895b))
* **types:** add CountResponseRelation enum type ([c5c6a3a](https://github.com/gitpod-io/gitpod-sdk-python/commit/c5c6a3a85b17dafe0bb879d42eb671f4601718b7))


### Bug Fixes

* **api:** rename executable_deny_list to veto_exec_policy in policies update ([8e6e434](https://github.com/gitpod-io/gitpod-sdk-python/commit/8e6e434949910725dcf3e0919e57f2f748acff15))
* **deps:** bump minimum typing-extensions version ([b542172](https://github.com/gitpod-io/gitpod-sdk-python/commit/b5421722237c860dbdf5a3490d13a8107ebf7849))
* **pydantic:** do not pass `by_alias` unless set ([f686038](https://github.com/gitpod-io/gitpod-sdk-python/commit/f6860389cff61faf455dc2a5ec96e85c88553ac3))
* sanitize endpoint path params ([89ccb9f](https://github.com/gitpod-io/gitpod-sdk-python/commit/89ccb9fe65cfb3c88e0ec2910809cb44bbc9e905))
* **types:** remove AGENT_EXECUTION values from Principal and ResourceRole enums ([36adf59](https://github.com/gitpod-io/gitpod-sdk-python/commit/36adf596f84d9ea0063185d7ade2ff5b4c723fb6))


### Chores

* **ci:** skip lint on metadata-only changes ([f958013](https://github.com/gitpod-io/gitpod-sdk-python/commit/f9580134a7bdbfbff1b67ee3d01f2868e839c502))
* **ci:** skip uploading artifacts on stainless-internal branches ([6955303](https://github.com/gitpod-io/gitpod-sdk-python/commit/69553031de097820152f561c7e300eceb8756df1))
* **docs:** add missing descriptions ([c10fa2e](https://github.com/gitpod-io/gitpod-sdk-python/commit/c10fa2e60f87bc25f37efa9923ebaac979abe6dd))
* **internal:** add request options to SSE classes ([17c6632](https://github.com/gitpod-io/gitpod-sdk-python/commit/17c6632b21cdf3fb082f74a6a3823cb210aa1757))
* **internal:** make `test_proxy_environment_variables` more resilient ([b5ee95d](https://github.com/gitpod-io/gitpod-sdk-python/commit/b5ee95d7dcc5a9da2ed73af7a7f896dd56c5b4a4))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([2520d14](https://github.com/gitpod-io/gitpod-sdk-python/commit/2520d14755b2be28dbb6b4335438482aca97a794))
* **internal:** move CountResponseRelation type to shared module ([641a91c](https://github.com/gitpod-io/gitpod-sdk-python/commit/641a91ccea854113f3d9ccea80ba22c2f82cad76))
* **internal:** regenerate SDK with no functional changes ([29406ce](https://github.com/gitpod-io/gitpod-sdk-python/commit/29406ce71a9aebfdc494ede23fa27b8023707288))
* **internal:** regenerate SDK with no functional changes ([22a7994](https://github.com/gitpod-io/gitpod-sdk-python/commit/22a7994b31d182bcdf03b2536fb0ad4c37e083fe))
* **internal:** regenerate SDK with no functional changes ([db63d58](https://github.com/gitpod-io/gitpod-sdk-python/commit/db63d58f926e9cb9c154c7d93720675c8876c653))
* **internal:** regenerate SDK with no functional changes ([d2529cf](https://github.com/gitpod-io/gitpod-sdk-python/commit/d2529cf9d3459f75411c550c0ae80a8a45cd8b4a))
* **internal:** regenerate SDK with no functional changes ([ca2f283](https://github.com/gitpod-io/gitpod-sdk-python/commit/ca2f283e1a7b4be40e7fe8da7c786b6270dc113e))
* **internal:** remove mock server code ([3c5deb3](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c5deb354f3c5059bac0bb2b50c288a7b40e2b7f))
* **internal:** tweak CI branches ([a7682f4](https://github.com/gitpod-io/gitpod-sdk-python/commit/a7682f4adc078236c5f7dba3806f533f76aaa814))
* **internal:** update gitignore ([43b2843](https://github.com/gitpod-io/gitpod-sdk-python/commit/43b28435b681f621d65390a3dc31e46db1a6ccb6))
* **internal:** update jsonl tests ([6d2b499](https://github.com/gitpod-io/gitpod-sdk-python/commit/6d2b4990c73692b942ae02d99577c119bd6a8b18))
* **test:** update skip reason message ([49175f9](https://github.com/gitpod-io/gitpod-sdk-python/commit/49175f922aa977681c528dc55920562433fcaaee))
* update mock server docs ([cef4896](https://github.com/gitpod-io/gitpod-sdk-python/commit/cef48965ac676afcc1adde238fc0a59c85ed0dac))


### Documentation

* **api:** add validation examples to timeout fields in policies/environments ([8ae9d6c](https://github.com/gitpod-io/gitpod-sdk-python/commit/8ae9d6cc242c17a4e608c289c34bfe0a1814ffb2))
* **api:** update annotations parameter examples in agents ([83d8cd3](https://github.com/gitpod-io/gitpod-sdk-python/commit/83d8cd363ceed43f1da66fe22ad6e766a987095a))
* **api:** update filter descriptions in groups role_assignment_list_params ([daf1ad5](https://github.com/gitpod-io/gitpod-sdk-python/commit/daf1ad5c2b42f7851566d8c32f5dda6f9313dd53))
* **api:** update min_size parameter docs in prebuilds warm pool methods ([ffe05fc](https://github.com/gitpod-io/gitpod-sdk-python/commit/ffe05fc8aeaab3a5128a5ebd469564b317777eca))

## 0.10.0 (2026-02-18)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** add audit_only field to executable_deny_list and veto ([82ede69](https://github.com/gitpod-io/gitpod-sdk-python/commit/82ede69962a1ae28dd47f881bf305dc6f457e794))
* **api:** add RUNNER_SIDE_AGENT to RunnerCapability type ([9375f78](https://github.com/gitpod-io/gitpod-sdk-python/commit/9375f7880e2d9e5db4fc57f4ed86c8b6ca5021fa))
* **api:** add WARMPOOL_ADMIN and WARMPOOL_VIEWER to ResourceRole ([5c316a6](https://github.com/gitpod-io/gitpod-sdk-python/commit/5c316a6cfc56e4ba44067ae33f33d0456474dae1))


### Bug Fixes

* **types:** rename ExecutableDenyList to VetoExecPolicy in organizations policies ([52f2760](https://github.com/gitpod-io/gitpod-sdk-python/commit/52f2760858e8e583cb0d5b68c2efffaf511193a8))


### Chores

* format all `api.md` files ([c52f954](https://github.com/gitpod-io/gitpod-sdk-python/commit/c52f954a3bda80d38af13cb8cc26a3d81831da76))
* **internal:** fix lint error on Python 3.14 ([2342adf](https://github.com/gitpod-io/gitpod-sdk-python/commit/2342adf3281e4eb7aa0584a60ea8b709ff97656c))

## 0.9.0 (2026-02-11)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** add bulk_create/bulk_delete/bulk_update methods to projects ([255bd90](https://github.com/gitpod-io/gitpod-sdk-python/commit/255bd90fadb010fbc75f2b38ec1e79b219cf06ef))

## 0.8.0 (2026-02-11)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.7.0...v0.8.0)

### Features

* [backend] Resource admin should be able to see all resource shares ([153d9ba](https://github.com/gitpod-io/gitpod-sdk-python/commit/153d9babce677adb9cda8b900b078ed7d16879b7))
* [SCIM] Configurable token expiration duration ([71eb2b6](https://github.com/gitpod-io/gitpod-sdk-python/commit/71eb2b62d685a409abe4a27129e0408758bc735f))
* [SCIM] Configurable token expiration duration ([16049ed](https://github.com/gitpod-io/gitpod-sdk-python/commit/16049ed4392e5551137a0bf7930b0a8ebcaa7b5e))
* **agent:** add annotations field to AgentExecution ([09c2210](https://github.com/gitpod-io/gitpod-sdk-python/commit/09c2210f258504cbebaed878233e2d5e06f939ec))
* **api:** add additional_scopes to organization SSO configuration ([07aa0cc](https://github.com/gitpod-io/gitpod-sdk-python/commit/07aa0cc02a4b65244104be04289c949bfb013c14))
* **api:** add announcement banner fields to organization proto ([1cbdaaa](https://github.com/gitpod-io/gitpod-sdk-python/commit/1cbdaaa69c1077d7d354991621af88f7e71e4df0))
* **api:** add derivedFromOrgRole field to RoleAssignment ([e1ed935](https://github.com/gitpod-io/gitpod-sdk-python/commit/e1ed9353e48590389e21fa38137280daeef56da9))
* **api:** add dev_runner_id to agents, dev_environment_id and provider to runners ([c345871](https://github.com/gitpod-io/gitpod-sdk-python/commit/c3458714c345048e05c74b213bcf087f3b977313))
* **api:** add exclude_group_id filter to organization list members ([008ae2b](https://github.com/gitpod-io/gitpod-sdk-python/commit/008ae2b90fef5c2f8eb5e1d624c9e5a2a6a1f83a))
* **api:** add ExecutableDenyList to environment and organization policy ([110c2ef](https://github.com/gitpod-io/gitpod-sdk-python/commit/110c2efc4f4d5dac2fa1209b7c85554060110889))
* **api:** add filters to ListPrebuilds for inventory page ([4bc3f9f](https://github.com/gitpod-io/gitpod-sdk-python/commit/4bc3f9f92f2de35c0cb1427df1af602014856000))
* **api:** add mcp_integrations field and type to agent_execution ([911140b](https://github.com/gitpod-io/gitpod-sdk-python/commit/911140bc7050b5e02daec1f207bbced61db39e0b))
* **api:** add opus 4.6 model variants to agent supported models ([71e660d](https://github.com/gitpod-io/gitpod-sdk-python/commit/71e660d25b7d164b2d37b09058aa3e74f445e5ca))
* **api:** add port access methods and organization admission level to environments ([af512f5](https://github.com/gitpod-io/gitpod-sdk-python/commit/af512f54181bc7da478f5e47b949715bec0e8b03))
* **api:** add ResourceRoleOrgAutomationsAdmin to ResourceRole enum ([320b285](https://github.com/gitpod-io/gitpod-sdk-python/commit/320b285f1fd8723e6c6fa0dc027812cff0891485))
* **api:** add ResourceRoleOrgGroupsAdmin to ResourceRole enum ([c2fceff](https://github.com/gitpod-io/gitpod-sdk-python/commit/c2fceff932dc786e8fc66d1fb44021e25f59c07e))
* **api:** add restrict_account_creation_to_scim field to organization policy ([c1272d1](https://github.com/gitpod-io/gitpod-sdk-python/commit/c1272d1a95dbcdb0366cff0c3158e3f9d4769f1a))
* **api:** add scope field and enum to environment secrets ([371f8f7](https://github.com/gitpod-io/gitpod-sdk-python/commit/371f8f7fc5e3fc882205b852aa684d5626c34e11))
* **api:** add user_ids filter to organization list members method ([5abdcae](https://github.com/gitpod-io/gitpod-sdk-python/commit/5abdcaecdc351d12e4715c1e4970d836173d6d9f))
* **api:** add warm pools resource to prebuilds ([b997cfe](https://github.com/gitpod-io/gitpod-sdk-python/commit/b997cfe8e95a7e55a645e7fa54446555ed0108e4))
* **api:** implement GetAnnouncementBanner and UpdateAnnouncementBanner handlers ([6482c1a](https://github.com/gitpod-io/gitpod-sdk-python/commit/6482c1a4b50742622a90815484c6b59020d196f6))
* **chat:** add Pylon identity verification for chat widget ([f7b7cb3](https://github.com/gitpod-io/gitpod-sdk-python/commit/f7b7cb37e2349ef60d26890c1a4cc72db34b32f8))
* **cli:** add --name flag to environment create command ([b292d8f](https://github.com/gitpod-io/gitpod-sdk-python/commit/b292d8f4fb2520ba65bb6701ac8507b16f56080e))
* **client:** add custom JSON encoder for extended type support ([48e0b49](https://github.com/gitpod-io/gitpod-sdk-python/commit/48e0b4951e34166dba1c29cd4e6b15fb2314b54e))
* **db:** add service_account_tokens table ([688cf2e](https://github.com/gitpod-io/gitpod-sdk-python/commit/688cf2e01a33ca12de9443d3857360d4223fa0f8))
* Introduce projects admin org role ([2777780](https://github.com/gitpod-io/gitpod-sdk-python/commit/2777780d987da76ab00f131c243b1ee69e39c901))
* **runner:** add capability check for ListSCMOrganizations ([4a87ef2](https://github.com/gitpod-io/gitpod-sdk-python/commit/4a87ef22bd88a83fb2eaa9255d9ae60bf8eee618))
* **types:** add RoleAssignment value to ResourceType enum ([d59ab98](https://github.com/gitpod-io/gitpod-sdk-python/commit/d59ab9810266a68d5b4cd31dd6da669d2691436f))


### Bug Fixes

* **api:** reject double-slash prefix in secret file paths ([fb4f63f](https://github.com/gitpod-io/gitpod-sdk-python/commit/fb4f63f9369cdcdb2cbc729bcd0a4bc0aa7b7745))


### Chores

* **ci:** upgrade `actions/github-script` ([d6a1726](https://github.com/gitpod-io/gitpod-sdk-python/commit/d6a1726d9806c8433ba7bc1612018bc84309147e))
* **internal:** bump dependencies ([330558d](https://github.com/gitpod-io/gitpod-sdk-python/commit/330558de3704863336c8b0bce5559237ef2d0e79))
* **internal:** formatting ([ecb24f2](https://github.com/gitpod-io/gitpod-sdk-python/commit/ecb24f297e892aecf91c294594f062c0baf6f8f5))
* update OpenAPI spec to e50946de8cddc549be7f7423903ad444632abce6 ([1176fce](https://github.com/gitpod-io/gitpod-sdk-python/commit/1176fce9b14b0bf657282228a20c222b2cb14ea5))


### Documentation

* **api:** clarify port_sharing_disabled behavior in organization policy ([2154cd8](https://github.com/gitpod-io/gitpod-sdk-python/commit/2154cd8abfa221c6c5aa4af9e85919fc927d888e))

## 0.7.0 (2026-01-21)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.6.0...v0.7.0)

### Features

* [api] Introduce RPCs to share resources with individual users ([df1cf39](https://github.com/gitpod-io/gitpod-sdk-python/commit/df1cf39a9c1b387c9e9313bfec68a97759762e0b))
* [api] sorting for `ListMembers` ([838e74c](https://github.com/gitpod-io/gitpod-sdk-python/commit/838e74c4da4b57590a6dd0af19bdd20faf7d2805))
* [backend] Adding direct_share field to groups ([78c0bdd](https://github.com/gitpod-io/gitpod-sdk-python/commit/78c0bddc838e217007729d723283f9e9cd04d9a2))
* [backend] Introduce role and member status filtering for `ListMembers` ([34fb372](https://github.com/gitpod-io/gitpod-sdk-python/commit/34fb372aef655ae57fc99d5b37e152c75d831af5))
* **agent:** add spec mode for planning before interactive implementation ([de6bee5](https://github.com/gitpod-io/gitpod-sdk-python/commit/de6bee5d7d337456f1a19de0659cd6957c7c1a9b))
* API for SCIM configuration management ([70becd4](https://github.com/gitpod-io/gitpod-sdk-python/commit/70becd4cd142fac4fc839018d52fb4cb93e17834))
* **api:** add CheckRepositoryAccess API for repository access validation ([b34ed1b](https://github.com/gitpod-io/gitpod-sdk-python/commit/b34ed1b8ecd39343ed02c5f376e9495775912140))
* **api:** add draft and state fields to PullRequest proto ([e0023da](https://github.com/gitpod-io/gitpod-sdk-python/commit/e0023da5a30344c2fc87ebce55e26101c4ad40b5))
* **api:** add inputs array to UserInputBlock proto ([8262825](https://github.com/gitpod-io/gitpod-sdk-python/commit/8262825c21be1de663b9a3aad29e9f9fe1cf219d))
* **api:** add ListSCMOrganizations endpoint ([9c8f7ea](https://github.com/gitpod-io/gitpod-sdk-python/commit/9c8f7eadd38bc0326ecf1be48706003fa258257c))
* **api:** add search, creator, and status filters to ListWorkflows ([ddd18c0](https://github.com/gitpod-io/gitpod-sdk-python/commit/ddd18c09beb0f24e076818783d2dae09ca9b9f8b))
* **api:** improve SearchRepositories pagination with next_page and total_count ([2847a10](https://github.com/gitpod-io/gitpod-sdk-python/commit/2847a10e6cbb09be83b012e8a6fcabd32f49e019))
* **automations:** add before_snapshot trigger type ([9cd272f](https://github.com/gitpod-io/gitpod-sdk-python/commit/9cd272f98f2215b834a841ca34c52ce04fd2898e))
* **client:** add support for binary request streaming ([be5a823](https://github.com/gitpod-io/gitpod-sdk-python/commit/be5a8235224ff1ecf25464e716191fbf3c7c7fb1))
* **dashboard:** show tier badge in org selector ([89fd8fe](https://github.com/gitpod-io/gitpod-sdk-python/commit/89fd8fef7f9de200e4aecd563c965d4209427052))
* Define SCIMConfiguration database schema ([03bd185](https://github.com/gitpod-io/gitpod-sdk-python/commit/03bd1858ec2aefbd4c20a71c206135c441afa99c))
* move agent mode from Spec to Status, add AgentModeChange signals ([a55115b](https://github.com/gitpod-io/gitpod-sdk-python/commit/a55115ba054078dcb689222cc150b2b1f56077bf))
* **secrets:** add ServiceAccountSecret entity with full support ([30e17c5](https://github.com/gitpod-io/gitpod-sdk-python/commit/30e17c55b991286527f64c8857b04dd9b5a2ba7b))


### Chores

* **internal:** update `actions/checkout` version ([53dcf30](https://github.com/gitpod-io/gitpod-sdk-python/commit/53dcf30cb41a6cbf30ce510b0b2d46cdd5895008))

## 0.6.0 (2026-01-09)

Full Changelog: [v0.5.2...v0.6.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.5.2...v0.6.0)

### Features

* **agent:** add group-based SCM tools access control ([9e23e57](https://github.com/gitpod-io/gitpod-sdk-python/commit/9e23e576ea787296c10f7edbb2a20bd9c47f5a4b))
* **api:** add ImageInput to UserInputBlock proto ([c1223c3](https://github.com/gitpod-io/gitpod-sdk-python/commit/c1223c3b9ae3ba1e2c088e0c740abc26648517c2))
* **api:** add recommended editors configuration to project settings ([5a4e222](https://github.com/gitpod-io/gitpod-sdk-python/commit/5a4e22212bb973211caf4cffa1dc40ec2a428ae1))
* **db:** add webhooks table with trigger reference ([d0bf7fa](https://github.com/gitpod-io/gitpod-sdk-python/commit/d0bf7faa87bcfd60d81cba84c50bd59ad0614c2f))
* **prebuild:** expose snapshot completion percentage in prebuild status ([05569c0](https://github.com/gitpod-io/gitpod-sdk-python/commit/05569c0e75fbd8fe107edb2119650030a1c21eed))
* **skills:** add organization-level skills support ([052b48a](https://github.com/gitpod-io/gitpod-sdk-python/commit/052b48ad57f64a7c09d05c898ea6638da0c886db))


### Bug Fixes

* use async_to_httpx_files in patch method ([af8d708](https://github.com/gitpod-io/gitpod-sdk-python/commit/af8d70859c29a43ffd66f949bb70712491458c3d))


### Chores

* **internal:** codegen related update ([c0e59ad](https://github.com/gitpod-io/gitpod-sdk-python/commit/c0e59ade25f1d13024bb78d5f525c8f55e52676c))
* **internal:** codegen related update ([34dd0fe](https://github.com/gitpod-io/gitpod-sdk-python/commit/34dd0fe4f13576840288a518b7c7c70f8d39d8f4))
* pin GitHub Actions to SHA ([36acefc](https://github.com/gitpod-io/gitpod-sdk-python/commit/36acefc6f9ab2cbbde739b885e0734a9f476115b))

## 0.5.2 (2025-12-16)

Full Changelog: [v0.5.1...v0.5.2](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.5.1...v0.5.2)

### Chores

* speedup initial import ([0cfe207](https://github.com/gitpod-io/gitpod-sdk-python/commit/0cfe207c87e568a6ca9ee6a5ff2251910b064444))

## 0.5.1 (2025-12-15)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.5.0...v0.5.1)

### Chores

* **internal:** add missing files argument to base client ([9d132f3](https://github.com/gitpod-io/gitpod-sdk-python/commit/9d132f33484aef2ab419052111d0d374ca7ce473))

## 0.5.0 (2025-12-15)

Full Changelog: [v0.4.4...v0.5.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.4.4...v0.5.0)

### Features

* **api:** RBAC APIs ([615e517](https://github.com/gitpod-io/gitpod-sdk-python/commit/615e517ec8e2b0f3e6816696dc3fe66e1f2ae99e))

## 0.4.4 (2025-12-15)

Full Changelog: [v0.4.3...v0.4.4](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.4.3...v0.4.4)

## 0.4.3 (2025-12-15)

Full Changelog: [v0.4.2...v0.4.3](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.4.2...v0.4.3)

## 0.4.2 (2025-12-15)

Full Changelog: [v0.4.1...v0.4.2](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.4.1...v0.4.2)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([cea547d](https://github.com/gitpod-io/gitpod-sdk-python/commit/cea547dff0e77fd9f3d913790e5bb85f7c566209))


### Chores

* add missing docstrings ([00778fe](https://github.com/gitpod-io/gitpod-sdk-python/commit/00778fe498f509982a2cee08c43ac9c9a4377e3e))

## 0.4.1 (2025-12-05)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.4.0...v0.4.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([597eb34](https://github.com/gitpod-io/gitpod-sdk-python/commit/597eb34a2f9f94a0ac4b6a8efd626ee253c7266f))
* compat with Python 3.14 ([11cab3b](https://github.com/gitpod-io/gitpod-sdk-python/commit/11cab3b8afc2dcd7c64b38fead6ffbad805a6f1c))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([d878bc6](https://github.com/gitpod-io/gitpod-sdk-python/commit/d878bc6a71bb2ac8e074019bee3db915d98a2312))
* ensure streams are always closed ([8e1d967](https://github.com/gitpod-io/gitpod-sdk-python/commit/8e1d96725dd7a77bd1abe0625824537eedc5b387))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([0581279](https://github.com/gitpod-io/gitpod-sdk-python/commit/0581279f1c20a01fd1b741fc56a5d66b724a8f66))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([620927e](https://github.com/gitpod-io/gitpod-sdk-python/commit/620927e38e8e968a7ee25cc4696be83b71b63dcc))
* do not install brew dependencies in ./scripts/bootstrap by default ([3fd8de4](https://github.com/gitpod-io/gitpod-sdk-python/commit/3fd8de42107e3941274833b72c4d17d3829dc6b9))
* **docs:** use environment variables for authentication in code snippets ([6435a45](https://github.com/gitpod-io/gitpod-sdk-python/commit/6435a4573f2c72303e813a55f6d30fc041afd80b))
* **internal/tests:** avoid race condition with implicit client cleanup ([2316010](https://github.com/gitpod-io/gitpod-sdk-python/commit/23160102a1df2cbcc7c9b4ab60f64860fca75af5))
* **internal:** codegen related update ([3487a7b](https://github.com/gitpod-io/gitpod-sdk-python/commit/3487a7b28a7fd3949d9cb898fc67939ec6ef8c1a))
* **internal:** detect missing future annotations with ruff ([98e718f](https://github.com/gitpod-io/gitpod-sdk-python/commit/98e718fd584a66b1cf64cf37baf4904935833b6c))
* **internal:** grammar fix (it's -&gt; its) ([ca7ec34](https://github.com/gitpod-io/gitpod-sdk-python/commit/ca7ec34adc07a3f66da8ca64398a218bf2fed68c))
* **internal:** update pydantic dependency ([986fdba](https://github.com/gitpod-io/gitpod-sdk-python/commit/986fdbaf9c668a21f87ab6b1368fb1f9b4dca9fc))
* **package:** drop Python 3.8 support ([86cbb78](https://github.com/gitpod-io/gitpod-sdk-python/commit/86cbb785d19b2286fdb0dc4c92d621b395a1c94b))
* **types:** change optional parameter type from NotGiven to Omit ([efa6bd7](https://github.com/gitpod-io/gitpod-sdk-python/commit/efa6bd70aed63ff891300fc1529575c76a18f104))
* update lockfile ([545bd86](https://github.com/gitpod-io/gitpod-sdk-python/commit/545bd8611860dc3a554ac238fbb8cae1fc471d6f))

## 0.4.0 (2025-12-05)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** gitpod -&gt; ona ([5ddf83b](https://github.com/gitpod-io/gitpod-sdk-python/commit/5ddf83b265d51f812b239afd3d9255f7fa8d2b6b))
* clean up environment call outs ([213fcdc](https://github.com/gitpod-io/gitpod-sdk-python/commit/213fcdc66361c6d258cb899f5ddbf56a1ebdaa62))
* **client:** add support for aiohttp ([9eeac4b](https://github.com/gitpod-io/gitpod-sdk-python/commit/9eeac4b8aa2066f8bd5a3720d13560ea0c031041))
* **client:** support file upload requests ([f986b23](https://github.com/gitpod-io/gitpod-sdk-python/commit/f986b231a55b031c7e6823d7ffc23e73c33afc72))
* improve future compat with pydantic v3 ([a52c037](https://github.com/gitpod-io/gitpod-sdk-python/commit/a52c03745925595327a938a16be5715d9675c9b6))


### Bug Fixes

* **ci:** correct conditional ([ee5b628](https://github.com/gitpod-io/gitpod-sdk-python/commit/ee5b628bf87cbb5844c4f1cc69e10f5a2bb1338f))
* **ci:** release-doctor — report correct token name ([0961324](https://github.com/gitpod-io/gitpod-sdk-python/commit/096132446b6f5672966ccdfce6d4eb007ee45773))
* **client:** correctly parse binary response | stream ([133ddee](https://github.com/gitpod-io/gitpod-sdk-python/commit/133ddeed84282ff4c41b9800cfa4e97951f7d207))
* **client:** don't send Content-Type header on GET requests ([92025c1](https://github.com/gitpod-io/gitpod-sdk-python/commit/92025c1f3b8d41d4c14b1217c6bfdd866ad89520))
* **parsing:** correctly handle nested discriminated unions ([f95762d](https://github.com/gitpod-io/gitpod-sdk-python/commit/f95762d56e17f372a2610c9dbbf7228401e18889))
* **parsing:** ignore empty metadata ([3901ec7](https://github.com/gitpod-io/gitpod-sdk-python/commit/3901ec7e4d11d8b3d2848cd3c28f1a64a203a5a3))
* **parsing:** parse extra field types ([e10d4fb](https://github.com/gitpod-io/gitpod-sdk-python/commit/e10d4fbc40758f2e00d81c52e269142de7ecf7d6))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([8a35255](https://github.com/gitpod-io/gitpod-sdk-python/commit/8a35255e8a9a579a5a2d014810d017dbcdeea87f))


### Chores

* **ci:** change upload type ([7801ba9](https://github.com/gitpod-io/gitpod-sdk-python/commit/7801ba9fe808fd6cd3088e1269f9dc4a00f169eb))
* **ci:** enable for pull requests ([615015e](https://github.com/gitpod-io/gitpod-sdk-python/commit/615015ecefc10a68d421f7f18eb8466e4afcfa10))
* **ci:** only run for pushes and fork pull requests ([8e3cd30](https://github.com/gitpod-io/gitpod-sdk-python/commit/8e3cd300ad4d0ff35b073c0aa98e46e537a299f6))
* **internal:** bump pinned h11 dep ([c55a48c](https://github.com/gitpod-io/gitpod-sdk-python/commit/c55a48c67150a3580a6dad3ff80996c6e4ae2847))
* **internal:** codegen related update ([e2efcf5](https://github.com/gitpod-io/gitpod-sdk-python/commit/e2efcf5c5289ada60c32c36d59987d933e40a6c6))
* **internal:** fix ruff target version ([d6156d2](https://github.com/gitpod-io/gitpod-sdk-python/commit/d6156d2ab264178dda14f8eed4496c3ff420fa94))
* **internal:** move mypy configurations to `pyproject.toml` file ([20ff2fd](https://github.com/gitpod-io/gitpod-sdk-python/commit/20ff2fdec396b41c230fd6f7ab6ffee8054e7b46))
* **internal:** update comment in script ([1aeeb0f](https://github.com/gitpod-io/gitpod-sdk-python/commit/1aeeb0fe71f4f10a76875770061da7e87c0bd000))
* **internal:** update conftest.py ([e1f69f3](https://github.com/gitpod-io/gitpod-sdk-python/commit/e1f69f382a1d5f99e71aa2e2ae559644f71b4352))
* **package:** mark python 3.13 as supported ([e580a61](https://github.com/gitpod-io/gitpod-sdk-python/commit/e580a61a67bba85d36aa04e99090a482de6a85a2))
* **project:** add settings file for vscode ([8ec9f41](https://github.com/gitpod-io/gitpod-sdk-python/commit/8ec9f413960970c9c46272d775e85b7cd2159a4c))
* **readme:** fix version rendering on pypi ([de1172d](https://github.com/gitpod-io/gitpod-sdk-python/commit/de1172d8dd3411f9ff5bf3e87c42c2c57ad1e602))
* **readme:** update badges ([2417444](https://github.com/gitpod-io/gitpod-sdk-python/commit/24174444a9b9ce67f5ef4590633f0380f2f7efee))
* **tests:** add tests for httpx client instantiation & proxies ([c03af6e](https://github.com/gitpod-io/gitpod-sdk-python/commit/c03af6ee2abc77132eda9ffad9e31a49e2dd59fb))
* **tests:** run tests in parallel ([6e0ed60](https://github.com/gitpod-io/gitpod-sdk-python/commit/6e0ed6062d5db6d5565b953c9991c0e8598775e1))
* **tests:** simplify `get_platform` test ([4726cc5](https://github.com/gitpod-io/gitpod-sdk-python/commit/4726cc56e22ec7883d51d433fda688679fe9d957))
* **tests:** skip some failing tests on the latest python versions ([4735291](https://github.com/gitpod-io/gitpod-sdk-python/commit/473529172a90e9ca731e0f9fc3ab881e4957d946))
* update @stainless-api/prism-cli to v5.15.0 ([3918e98](https://github.com/gitpod-io/gitpod-sdk-python/commit/3918e98029a9a2e1381f1488c75c14d8e3e16bbd))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([28e4f0d](https://github.com/gitpod-io/gitpod-sdk-python/commit/28e4f0da8237a7823e79b9beea870e9689261d57))

## 0.3.0 (2025-06-06)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.2.1...v0.3.0)

### Features

* **api:** manual updates ([640479a](https://github.com/gitpod-io/gitpod-sdk-python/commit/640479ad011cec5bc45b8036f92ec07008e48d76))
* **api:** manual updates ([72320f5](https://github.com/gitpod-io/gitpod-sdk-python/commit/72320f5101905608aa1819520251813c28a498ab))
* **api:** manual updates ([530d80c](https://github.com/gitpod-io/gitpod-sdk-python/commit/530d80c68524c0ff5adfdcc157fafdf44f69a2c8))
* **api:** manual updates ([2717e93](https://github.com/gitpod-io/gitpod-sdk-python/commit/2717e930a0978b5c596d4486464e6faf5e3121b9))
* **api:** manual updates ([416c2ef](https://github.com/gitpod-io/gitpod-sdk-python/commit/416c2ef62dd99f6b6690d9e1f311019244f2dc78))
* **api:** manual updates ([#61](https://github.com/gitpod-io/gitpod-sdk-python/issues/61)) ([f8a2a44](https://github.com/gitpod-io/gitpod-sdk-python/commit/f8a2a44972841b5799dddf39cefb1e75a29e67be))
* **api:** manual updates ([#64](https://github.com/gitpod-io/gitpod-sdk-python/issues/64)) ([f29b9ba](https://github.com/gitpod-io/gitpod-sdk-python/commit/f29b9ba65db6e3c1737c2d781e82ac3bcd457e3a))
* **client:** allow passing `NotGiven` for body ([#63](https://github.com/gitpod-io/gitpod-sdk-python/issues/63)) ([a62be8a](https://github.com/gitpod-io/gitpod-sdk-python/commit/a62be8a6e5ce5af0aeaec008db7f0a214222515d))


### Bug Fixes

* **ci:** ensure pip is always available ([#75](https://github.com/gitpod-io/gitpod-sdk-python/issues/75)) ([2a3ae1d](https://github.com/gitpod-io/gitpod-sdk-python/commit/2a3ae1d9237518fbdc267f64dcca813ed6251192))
* **ci:** remove publishing patch ([#76](https://github.com/gitpod-io/gitpod-sdk-python/issues/76)) ([fc6ffe9](https://github.com/gitpod-io/gitpod-sdk-python/commit/fc6ffe9aa684e00af4a44001a2617452df84f106))
* **client:** mark some request bodies as optional ([a62be8a](https://github.com/gitpod-io/gitpod-sdk-python/commit/a62be8a6e5ce5af0aeaec008db7f0a214222515d))
* **perf:** optimize some hot paths ([4a25116](https://github.com/gitpod-io/gitpod-sdk-python/commit/4a251160e74c27a9826fd9146ee630981423994f))
* **perf:** skip traversing types for NotGiven values ([655645b](https://github.com/gitpod-io/gitpod-sdk-python/commit/655645b8376a92c4a15e985fdeb862a0837cdda2))
* **pydantic v1:** more robust ModelField.annotation check ([6b28a69](https://github.com/gitpod-io/gitpod-sdk-python/commit/6b28a69cc3af92639a9e90f8c949ab55a16baeea))
* **types:** handle more discriminated union shapes ([#74](https://github.com/gitpod-io/gitpod-sdk-python/issues/74)) ([e2efe2b](https://github.com/gitpod-io/gitpod-sdk-python/commit/e2efe2bf0a2547b937f8d459172c9b3fd172fd32))


### Chores

* broadly detect json family of content-type headers ([a4e4e7a](https://github.com/gitpod-io/gitpod-sdk-python/commit/a4e4e7a6c31a7109c129cd21ea86921c212af657))
* **ci:** add timeout thresholds for CI jobs ([9112f34](https://github.com/gitpod-io/gitpod-sdk-python/commit/9112f34a032563f4805ff367ea46a7376560e4a3))
* **ci:** only use depot for staging repos ([e00a169](https://github.com/gitpod-io/gitpod-sdk-python/commit/e00a1694e5677db460b8046c9b42b5916a737891))
* **client:** minor internal fixes ([48341b1](https://github.com/gitpod-io/gitpod-sdk-python/commit/48341b1e44daa967e37e6a9b85429d8231177c81))
* **docs:** update client docstring ([#68](https://github.com/gitpod-io/gitpod-sdk-python/issues/68)) ([65a92c5](https://github.com/gitpod-io/gitpod-sdk-python/commit/65a92c5c0cb39bf290d24567450a30eda21a7e5b))
* fix typos ([#77](https://github.com/gitpod-io/gitpod-sdk-python/issues/77)) ([ad69954](https://github.com/gitpod-io/gitpod-sdk-python/commit/ad69954af16f51fb4f89a932d0bbc50501b40119))
* **internal:** base client updates ([4615096](https://github.com/gitpod-io/gitpod-sdk-python/commit/4615096ade22d29d38d419d18a076ca020dc5563))
* **internal:** bump pyright version ([9073aa6](https://github.com/gitpod-io/gitpod-sdk-python/commit/9073aa6de0e29f0fdf01e1463a4d513de695fcf3))
* **internal:** bump rye to 0.44.0 ([#73](https://github.com/gitpod-io/gitpod-sdk-python/issues/73)) ([64be852](https://github.com/gitpod-io/gitpod-sdk-python/commit/64be85212587bec1388214453bd4d7f0ddff57a4))
* **internal:** codegen related update ([0067daf](https://github.com/gitpod-io/gitpod-sdk-python/commit/0067daffa78169feae6f0c5b6c7d3c94e7fb0a9c))
* **internal:** codegen related update ([#70](https://github.com/gitpod-io/gitpod-sdk-python/issues/70)) ([317e72c](https://github.com/gitpod-io/gitpod-sdk-python/commit/317e72c74e544cb15945bd610a2ddadebd76be1a))
* **internal:** codegen related update ([#72](https://github.com/gitpod-io/gitpod-sdk-python/issues/72)) ([a8f27cc](https://github.com/gitpod-io/gitpod-sdk-python/commit/a8f27ccf962b45cc626331ee5ead0a0560235ee6))
* **internal:** expand CI branch coverage ([c99fbf1](https://github.com/gitpod-io/gitpod-sdk-python/commit/c99fbf1293bfae482b24cfcdfdcff9508bea73f3))
* **internal:** fix list file params ([4a852b4](https://github.com/gitpod-io/gitpod-sdk-python/commit/4a852b476184043f3508591751a6ccdadf0cc8e8))
* **internal:** import reformatting ([702e260](https://github.com/gitpod-io/gitpod-sdk-python/commit/702e26060fcc0373063c0b1a873e7c53dbb11f8f))
* **internal:** minor formatting changes ([759ff42](https://github.com/gitpod-io/gitpod-sdk-python/commit/759ff42ae1059b7697b94e5fa04dc861addd7439))
* **internal:** properly set __pydantic_private__ ([#66](https://github.com/gitpod-io/gitpod-sdk-python/issues/66)) ([ce1db49](https://github.com/gitpod-io/gitpod-sdk-python/commit/ce1db49b85a64443a5a2143a5b00224d0e3192d1))
* **internal:** reduce CI branch coverage ([f9fb625](https://github.com/gitpod-io/gitpod-sdk-python/commit/f9fb625d504b60d4374078e2be8320c2a9a3018a))
* **internal:** refactor retries to not use recursion ([fba2a60](https://github.com/gitpod-io/gitpod-sdk-python/commit/fba2a601a842c7a7d1c211cbd8cc3dcdc5343492))
* **internal:** remove extra empty newlines ([#71](https://github.com/gitpod-io/gitpod-sdk-python/issues/71)) ([5166c0c](https://github.com/gitpod-io/gitpod-sdk-python/commit/5166c0c48aaa8e59c90d1c23c1dd1bd3d93ba6d9))
* **internal:** remove trailing character ([#78](https://github.com/gitpod-io/gitpod-sdk-python/issues/78)) ([140ac8b](https://github.com/gitpod-io/gitpod-sdk-python/commit/140ac8b28ddda23e63830cf6049d13498efd015d))
* **internal:** remove unused http client options forwarding ([#69](https://github.com/gitpod-io/gitpod-sdk-python/issues/69)) ([69a6bde](https://github.com/gitpod-io/gitpod-sdk-python/commit/69a6bde0c2630357e6bcbb26d3848a1679e62bfe))
* **internal:** slight transform perf improvement ([#80](https://github.com/gitpod-io/gitpod-sdk-python/issues/80)) ([62166e9](https://github.com/gitpod-io/gitpod-sdk-python/commit/62166e9543adfd3ab32fb403c9ab3a26b767f618))
* **internal:** update models test ([55f3b64](https://github.com/gitpod-io/gitpod-sdk-python/commit/55f3b64a6d9a69cd0cf04b4c71b606ec96c99eab))
* **internal:** update pyright settings ([d924d39](https://github.com/gitpod-io/gitpod-sdk-python/commit/d924d395581530e38250a0e1c906ce72939b9837))
* **internal:** variable name and test updates ([#79](https://github.com/gitpod-io/gitpod-sdk-python/issues/79)) ([7de371c](https://github.com/gitpod-io/gitpod-sdk-python/commit/7de371cb2912224280342f8793b181feaed8129a))
* **tests:** improve enum examples ([#81](https://github.com/gitpod-io/gitpod-sdk-python/issues/81)) ([7b5fc94](https://github.com/gitpod-io/gitpod-sdk-python/commit/7b5fc94fa15074885fde8cea674bd5ad0bbfb2a8))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#67](https://github.com/gitpod-io/gitpod-sdk-python/issues/67)) ([cfce519](https://github.com/gitpod-io/gitpod-sdk-python/commit/cfce51963c3e840969f7395d1fd448d3fe33871e))

## 0.2.1 (2025-02-18)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.2.0...v0.2.1)

### Features

* **api:** add events streaming ([1d7a848](https://github.com/gitpod-io/gitpod-sdk-python/commit/1d7a848908ba3cb5c527bc6253c19e5a84a28b18))
* **api:** dedupe paginations ([75dc8c4](https://github.com/gitpod-io/gitpod-sdk-python/commit/75dc8c43b9ef8453cac3d9f18aafaa5deffca48f))
* **api:** fix pagination field names ([af22da1](https://github.com/gitpod-io/gitpod-sdk-python/commit/af22da11015915a96f68f74851abc7442fc4a0bf))
* **api:** manual updates ([0f00366](https://github.com/gitpod-io/gitpod-sdk-python/commit/0f00366da2833f31a9f298ac6c2ae980c1a6db99))
* **api:** manual updates ([4d19977](https://github.com/gitpod-io/gitpod-sdk-python/commit/4d199779647d6fafb2a1a26872b5a72c4b3378b6))
* **api:** manual updates ([#34](https://github.com/gitpod-io/gitpod-sdk-python/issues/34)) ([0641e82](https://github.com/gitpod-io/gitpod-sdk-python/commit/0641e82f55caac2e7ddef3bd64dc69c132f3b20d))
* **api:** manual updates ([#57](https://github.com/gitpod-io/gitpod-sdk-python/issues/57)) ([7bfbd45](https://github.com/gitpod-io/gitpod-sdk-python/commit/7bfbd456dfc8719532ff255b1c5ce7294115d2a4))
* **api:** pagination config ([c407e2e](https://github.com/gitpod-io/gitpod-sdk-python/commit/c407e2eaadda4d1ccbba6065235eac03a2332c48))
* **api:** properly produce empty request bodies ([#4](https://github.com/gitpod-io/gitpod-sdk-python/issues/4)) ([58d9393](https://github.com/gitpod-io/gitpod-sdk-python/commit/58d93934944affe142520d167b34068973a91ee8))
* **api:** try to fix updateenvironmentrequest ([#8](https://github.com/gitpod-io/gitpod-sdk-python/issues/8)) ([682243a](https://github.com/gitpod-io/gitpod-sdk-python/commit/682243ad64a55a79a59d63328d41057a922c9d2b))
* **api:** update to latest changes ([#10](https://github.com/gitpod-io/gitpod-sdk-python/issues/10)) ([cec21eb](https://github.com/gitpod-io/gitpod-sdk-python/commit/cec21ebbe15b2a5bbce13a4bffe40ab57803e0ae))
* **api:** update via SDK Studio ([3e66ecc](https://github.com/gitpod-io/gitpod-sdk-python/commit/3e66ecc1e5b3f7495b143f9fb31df85d24b871c6))
* **api:** update via SDK Studio ([66db733](https://github.com/gitpod-io/gitpod-sdk-python/commit/66db73366f6edaf7f0b21c1a88ec230b8650423d))
* **api:** update via SDK Studio ([d20eaba](https://github.com/gitpod-io/gitpod-sdk-python/commit/d20eaba8a2034c60b7957e74b1b060305102a520))
* **api:** update via SDK Studio ([b418dbe](https://github.com/gitpod-io/gitpod-sdk-python/commit/b418dbed6ce6c7e3a6eeee211f3391342cdc9d51))
* **api:** update via SDK Studio ([06c4b10](https://github.com/gitpod-io/gitpod-sdk-python/commit/06c4b10fff0b115550b0ab3a5fa106348d3868d4))
* **api:** update via SDK Studio ([5b25656](https://github.com/gitpod-io/gitpod-sdk-python/commit/5b2565694ed495e564f948078c02dd46efe8fadf))
* **api:** update via SDK Studio ([ea67c8c](https://github.com/gitpod-io/gitpod-sdk-python/commit/ea67c8c3e4ed067a049153a6807051bdf6f64cff))
* **api:** update via SDK Studio ([974fb63](https://github.com/gitpod-io/gitpod-sdk-python/commit/974fb635622cc790b134afa0e374e27951ab59b4))
* **api:** update via SDK Studio ([4e32701](https://github.com/gitpod-io/gitpod-sdk-python/commit/4e3270181d05a023bec2afc835dea83fcdcec3b2))
* **api:** update via SDK Studio ([f8ce60d](https://github.com/gitpod-io/gitpod-sdk-python/commit/f8ce60dbadb28a8d29184ac561f5c0608e23e5a0))
* **api:** update via SDK Studio ([87524c3](https://github.com/gitpod-io/gitpod-sdk-python/commit/87524c331c989fa4debc93bede3e16659f94ec62))
* **api:** update via SDK Studio ([2ac41b3](https://github.com/gitpod-io/gitpod-sdk-python/commit/2ac41b3c8889105bd7d5c9a052468646bd670252))
* **api:** update via SDK Studio ([7b2f2cf](https://github.com/gitpod-io/gitpod-sdk-python/commit/7b2f2cf872b573c4945ab7eb83e1011dcd082f06))
* **api:** update via SDK Studio ([c8930ae](https://github.com/gitpod-io/gitpod-sdk-python/commit/c8930ae28eb3d89dd32ca1db15d1bd4bd0423498))
* **api:** update via SDK Studio ([e42265e](https://github.com/gitpod-io/gitpod-sdk-python/commit/e42265e20f8fb254f4ea31f4f868de669dd31475))
* **api:** update via SDK Studio ([dd8ecd8](https://github.com/gitpod-io/gitpod-sdk-python/commit/dd8ecd84a27bb9c9701c269e05300a7d2d4e5708))
* **api:** update via SDK Studio ([8d5f640](https://github.com/gitpod-io/gitpod-sdk-python/commit/8d5f640dd221b455794a8cf40b2071af0467d3f5))
* **api:** update via SDK Studio ([e27af94](https://github.com/gitpod-io/gitpod-sdk-python/commit/e27af94de0c010b0970f3badad10ee35034dfe1d))
* **api:** update via SDK Studio ([48a5274](https://github.com/gitpod-io/gitpod-sdk-python/commit/48a5274bbc3678b4a0cc74679efa9884acb258df))
* **api:** update via SDK Studio ([2139387](https://github.com/gitpod-io/gitpod-sdk-python/commit/2139387ad0c36be18b31a0f3446c39c974637520))
* **api:** update via SDK Studio ([afa5045](https://github.com/gitpod-io/gitpod-sdk-python/commit/afa504592f2b73d450dfc7e9bd074fa22c23be7e))
* **auth:** Add SCM authentication support for repository access ([#44](https://github.com/gitpod-io/gitpod-sdk-python/issues/44)) ([d400b3f](https://github.com/gitpod-io/gitpod-sdk-python/commit/d400b3f8cd5334bbd2feeee80a57114012372da6))
* **client:** send `X-Stainless-Read-Timeout` header ([#6](https://github.com/gitpod-io/gitpod-sdk-python/issues/6)) ([a49ba54](https://github.com/gitpod-io/gitpod-sdk-python/commit/a49ba542e66b2373afea100eb704fbdfc3860823))
* **jsonl:** add .close() method ([#11](https://github.com/gitpod-io/gitpod-sdk-python/issues/11)) ([bb42526](https://github.com/gitpod-io/gitpod-sdk-python/commit/bb425268e5725cf8b93b88bf0610929f9f8d73a0))
* pagination responses ([d009d64](https://github.com/gitpod-io/gitpod-sdk-python/commit/d009d64229f53e4f271799d273bbbae26fb3520b))


### Bug Fixes

* **api:** better support union schemas with common properties ([ad416b2](https://github.com/gitpod-io/gitpod-sdk-python/commit/ad416b216575ab7c015ab984dd94a72b240ad467))
* **client:** compat with new httpx 0.28.0 release ([abc0621](https://github.com/gitpod-io/gitpod-sdk-python/commit/abc0621222e659f182967b3ca147280f244e1fc4))
* **client:** only call .close() when needed ([bbb6747](https://github.com/gitpod-io/gitpod-sdk-python/commit/bbb6747ad4d09e9066cda67947fea40937d89bd2))
* correctly handle deserialising `cls` fields ([df55d8a](https://github.com/gitpod-io/gitpod-sdk-python/commit/df55d8a1decd0514c24033b9f2615616a1ae2292))
* **jsonl:** lower chunk size ([#12](https://github.com/gitpod-io/gitpod-sdk-python/issues/12)) ([1d52633](https://github.com/gitpod-io/gitpod-sdk-python/commit/1d52633086277672510cc94e52d71e2dd87a695d))
* pagination example ([8ddfb41](https://github.com/gitpod-io/gitpod-sdk-python/commit/8ddfb41ab1b872e2d8535194801826e88e7dee08))
* pagination response ([ba50863](https://github.com/gitpod-io/gitpod-sdk-python/commit/ba50863a1b9e11dcaafa657475081147f2fefd23))
* **tests:** disable mock tests ([#5](https://github.com/gitpod-io/gitpod-sdk-python/issues/5)) ([5815445](https://github.com/gitpod-io/gitpod-sdk-python/commit/58154457f8d42aa1ebf896c3f2e4fcbe9b967b0e))
* **tests:** disable test mocks ([#3](https://github.com/gitpod-io/gitpod-sdk-python/issues/3)) ([fcdbd22](https://github.com/gitpod-io/gitpod-sdk-python/commit/fcdbd2292fa2a1ace4f62f0e6e62c3781648ffee))
* **tests:** make test_get_platform less flaky ([51968d4](https://github.com/gitpod-io/gitpod-sdk-python/commit/51968d4b351b54b5b402d8a77b37249205fe3681))


### Chores

* add missing isclass check ([ff7cbaa](https://github.com/gitpod-io/gitpod-sdk-python/commit/ff7cbaa4807baf6951a6317880ab894949129e85))
* go live ([#1](https://github.com/gitpod-io/gitpod-sdk-python/issues/1)) ([49112f9](https://github.com/gitpod-io/gitpod-sdk-python/commit/49112f9912435229e57494ee2f09757918b2f1c7))
* go live ([#14](https://github.com/gitpod-io/gitpod-sdk-python/issues/14)) ([0cfb0dd](https://github.com/gitpod-io/gitpod-sdk-python/commit/0cfb0ddb1c8919e647e3cb56c08c989b0a94979a))
* **internal:** avoid pytest-asyncio deprecation warning ([3c00c53](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c00c53a00ff67157829da89bbbaceae142a411e))
* **internal:** bump httpx dependency ([e160bd9](https://github.com/gitpod-io/gitpod-sdk-python/commit/e160bd9a691017994b8704cca5eaaef0d0344940))
* **internal:** bump pydantic dependency ([5ce555b](https://github.com/gitpod-io/gitpod-sdk-python/commit/5ce555ba5ccdfa37a62c891e46a1758e1445369c))
* **internal:** bump pyright ([aba3b34](https://github.com/gitpod-io/gitpod-sdk-python/commit/aba3b34b382753596f0e3bbc211221b307d2d32c))
* **internal:** change default timeout to an int ([6430f4c](https://github.com/gitpod-io/gitpod-sdk-python/commit/6430f4cde5fb665c32501880ff06127b348e8b31))
* **internal:** codegen related update ([ec5eb7e](https://github.com/gitpod-io/gitpod-sdk-python/commit/ec5eb7e1ab7ce34c1f359300fdc1354e1d5cf549))
* **internal:** codegen related update ([497ae18](https://github.com/gitpod-io/gitpod-sdk-python/commit/497ae18d5624499a7c907f4689a8879b7c1d40b1))
* **internal:** codegen related update ([c9288d5](https://github.com/gitpod-io/gitpod-sdk-python/commit/c9288d535936274a7927b2bb2bf7e424e5b1e8b4))
* **internal:** codegen related update ([cb8475b](https://github.com/gitpod-io/gitpod-sdk-python/commit/cb8475b8084ade988b2861b636a432d45fb3b2ff))
* **internal:** codegen related update ([26b774b](https://github.com/gitpod-io/gitpod-sdk-python/commit/26b774b422be3b8f51ab25facff1c75c89257991))
* **internal:** codegen related update ([0f3b621](https://github.com/gitpod-io/gitpod-sdk-python/commit/0f3b6216e5c5fe1155fa8ae28fb8a81c65421267))
* **internal:** codegen related update ([0dab9d3](https://github.com/gitpod-io/gitpod-sdk-python/commit/0dab9d38924656bf9c2132a320d1233bc61e696a))
* **internal:** codegen related update ([838ff11](https://github.com/gitpod-io/gitpod-sdk-python/commit/838ff11b1d62ddc7148953e73262a35e1ec575ec))
* **internal:** codegen related update ([fafa29d](https://github.com/gitpod-io/gitpod-sdk-python/commit/fafa29d268068e422e5b774eacdd2faedbe32f39))
* **internal:** codegen related update ([80c8bbf](https://github.com/gitpod-io/gitpod-sdk-python/commit/80c8bbfa9f757e97878d336cd9cd7babe5d52d6b))
* **internal:** codegen related update ([36c6d5e](https://github.com/gitpod-io/gitpod-sdk-python/commit/36c6d5eb17f40adb63a29f22d89afa8eca9c0677))
* **internal:** exclude mypy from running on tests ([cae2176](https://github.com/gitpod-io/gitpod-sdk-python/commit/cae2176e0a99d1094f797fb49baab2435c04d5f6))
* **internal:** fix compat model_dump method when warnings are passed ([ee87f96](https://github.com/gitpod-io/gitpod-sdk-python/commit/ee87f963bab5e9ac07b3a9fb4c40f46ca3a07613))
* **internal:** fix some typos ([c0f7e58](https://github.com/gitpod-io/gitpod-sdk-python/commit/c0f7e58307c3602499e72354aee6d2ada1e15528))
* **internal:** fix type traversing dictionary params ([#7](https://github.com/gitpod-io/gitpod-sdk-python/issues/7)) ([d91bc6c](https://github.com/gitpod-io/gitpod-sdk-python/commit/d91bc6c0489e0c62d9c8ccaf6024341816e95491))
* **internal:** minor formatting changes ([2273048](https://github.com/gitpod-io/gitpod-sdk-python/commit/2273048b7dbc282f31edf563d56ff8dd223969d8))
* **internal:** minor type handling changes ([#9](https://github.com/gitpod-io/gitpod-sdk-python/issues/9)) ([83e7e59](https://github.com/gitpod-io/gitpod-sdk-python/commit/83e7e59f06f3ee5cc755adc31df189c682e795ce))
* **internal:** remove some duplicated imports ([8e6cc74](https://github.com/gitpod-io/gitpod-sdk-python/commit/8e6cc74d2e16297d05cd9cc233e4d79fdff64930))
* **internal:** update examples ([d652f4e](https://github.com/gitpod-io/gitpod-sdk-python/commit/d652f4e1ab70a731eff04beb3ff0f7c471dbcacf))
* **internal:** updated imports ([d31547b](https://github.com/gitpod-io/gitpod-sdk-python/commit/d31547b97db1baea0383ecb8a86e65270a093b77))
* make the `Omit` type public ([cf43176](https://github.com/gitpod-io/gitpod-sdk-python/commit/cf4317618f0cc177f812781d62bd454afa279f45))
* rebuild project due to codegen change ([4c930a5](https://github.com/gitpod-io/gitpod-sdk-python/commit/4c930a5227bbec3f5a3d378ababf01ae8d4cedb3))
* rebuild project due to codegen change ([b7129db](https://github.com/gitpod-io/gitpod-sdk-python/commit/b7129db829b29adc2fbcf0eebdfc9f97e80d74c6))
* rebuild project due to codegen change ([56f37cb](https://github.com/gitpod-io/gitpod-sdk-python/commit/56f37cb299889d38a458cacc659c21df8bf14fbe))
* rebuild project due to codegen change ([710a64b](https://github.com/gitpod-io/gitpod-sdk-python/commit/710a64bcff5107c7180c9c994594c30a65e182cb))
* remove now unused `cached-property` dep ([b66de02](https://github.com/gitpod-io/gitpod-sdk-python/commit/b66de02aeb1dfe216c3c6f4687db973de79f03d2))
* security config ([3c91d8f](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c91d8f00626733cdfb925c0382b994f287b8c33))


### Documentation

* add info log level to readme ([aebe445](https://github.com/gitpod-io/gitpod-sdk-python/commit/aebe445be3e15f9773dad03ee9b3f565f3c7273b))
* fix typos ([35edab0](https://github.com/gitpod-io/gitpod-sdk-python/commit/35edab0b4da50551371b866f4a24a5c520fa9264))
* **raw responses:** fix duplicate `the` ([5d59373](https://github.com/gitpod-io/gitpod-sdk-python/commit/5d5937373485b2a0293d9ebd0ca949d9ed8da26f))
* **readme:** example snippet for client context manager ([b8180b3](https://github.com/gitpod-io/gitpod-sdk-python/commit/b8180b3266fe57a68e3e72af355bb7cc898b8bf2))
* **readme:** fix http client proxies example ([079665c](https://github.com/gitpod-io/gitpod-sdk-python/commit/079665c9ce58df2e2f7c77cb6b610fdb0dc62c43))

## 0.2.0 (2025-02-18)

Full Changelog: [v0.1.6...v0.2.0](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.6...v0.2.0)

### Features

* feat(auth): Add SCM authentication support for repository access ([#44](https://github.com/gitpod-io/gitpod-sdk-python/issues/44)) ([6a5dc38](https://github.com/gitpod-io/gitpod-sdk-python/commit/6a5dc385ea6a8ea0f5ea9ef18c61380d6c617221))

## 0.1.6 (2025-02-18)

Full Changelog: [v0.1.5...v0.1.6](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.5...v0.1.6)

### Features

* **api:** manual updates ([#52](https://github.com/gitpod-io/gitpod-sdk-python/issues/52)) ([0f10942](https://github.com/gitpod-io/gitpod-sdk-python/commit/0f1094287dd9f709e0f6b63760f0d7b6fa7b135a))

## 0.1.5 (2025-02-18)

Full Changelog: [v0.1.4...v0.1.5](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.4...v0.1.5)

### Features

* **api:** manual updates ([#49](https://github.com/gitpod-io/gitpod-sdk-python/issues/49)) ([3e29d91](https://github.com/gitpod-io/gitpod-sdk-python/commit/3e29d910f0c75eacbe0693cc82c68063f2782fc2))

## 0.1.4 (2025-02-18)

Full Changelog: [v0.1.3...v0.1.4](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.3...v0.1.4)

### Features

* **api:** manual updates ([#46](https://github.com/gitpod-io/gitpod-sdk-python/issues/46)) ([50e6697](https://github.com/gitpod-io/gitpod-sdk-python/commit/50e669758fceea61ffd62bd0e463f9b588c11000))

## 0.1.3 (2025-02-14)

Full Changelog: [v0.1.2...v0.1.3](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.2...v0.1.3)

### Chores

* **internal:** add jsonl unit tests ([#43](https://github.com/gitpod-io/gitpod-sdk-python/issues/43)) ([8641b53](https://github.com/gitpod-io/gitpod-sdk-python/commit/8641b53116b20dd8e329f229afd84ec6a100fcef))
* **internal:** codegen related update ([#41](https://github.com/gitpod-io/gitpod-sdk-python/issues/41)) ([e5dceda](https://github.com/gitpod-io/gitpod-sdk-python/commit/e5dceda109bb01cf538dce83c3ab16d60461eb3d))

## 0.1.2 (2025-02-14)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.1...v0.1.2)

### Features

* **api:** manual updates ([#39](https://github.com/gitpod-io/gitpod-sdk-python/issues/39)) ([31f6c01](https://github.com/gitpod-io/gitpod-sdk-python/commit/31f6c01e50663c19a4e11808458b4bbd3fb38ead))
* **api:** Organizations Open API docs ([#37](https://github.com/gitpod-io/gitpod-sdk-python/issues/37)) ([ed6623d](https://github.com/gitpod-io/gitpod-sdk-python/commit/ed6623dbad5cf3605f8d5e3d07450cc30576ad0f))

## 0.1.1 (2025-02-14)

Full Changelog: [v0.1.0-alpha.3...v0.1.1](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.0-alpha.3...v0.1.1)

### Features

* **api:** manual updates ([#34](https://github.com/gitpod-io/gitpod-sdk-python/issues/34)) ([fb5ff55](https://github.com/gitpod-io/gitpod-sdk-python/commit/fb5ff55a252bf6d6bee4dd33b732680cf3100a40))

## 0.1.0-alpha.3 (2025-02-14)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** manual updates ([#24](https://github.com/gitpod-io/gitpod-sdk-python/issues/24)) ([b14af5b](https://github.com/gitpod-io/gitpod-sdk-python/commit/b14af5b14f013a2d966b6dca24abcc45975555e5))
* **api:** manual updates ([#25](https://github.com/gitpod-io/gitpod-sdk-python/issues/25)) ([a13ae46](https://github.com/gitpod-io/gitpod-sdk-python/commit/a13ae465471d0323a2151fc904c8214f295e5a90))
* **api:** manual updates ([#28](https://github.com/gitpod-io/gitpod-sdk-python/issues/28)) ([b763659](https://github.com/gitpod-io/gitpod-sdk-python/commit/b763659e5a226b94311d5f898534794879b279f8))
* **api:** manual updates ([#30](https://github.com/gitpod-io/gitpod-sdk-python/issues/30)) ([45bdb31](https://github.com/gitpod-io/gitpod-sdk-python/commit/45bdb315c9e912833b335244ac1fdb7737c423c2))
* **api:** update examples ([#22](https://github.com/gitpod-io/gitpod-sdk-python/issues/22)) ([a3a0b9d](https://github.com/gitpod-io/gitpod-sdk-python/commit/a3a0b9dbb81bc5915ca65948fc570b406b2b587e))
* **api:** update with latest API spec ([#27](https://github.com/gitpod-io/gitpod-sdk-python/issues/27)) ([80f6e19](https://github.com/gitpod-io/gitpod-sdk-python/commit/80f6e194b049fa48e82fe310c9c56e632588bfb9))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#31](https://github.com/gitpod-io/gitpod-sdk-python/issues/31)) ([507a01e](https://github.com/gitpod-io/gitpod-sdk-python/commit/507a01eb2eaed68da316448a12a98d13034b57f7))


### Chores

* **internal:** update client tests ([#26](https://github.com/gitpod-io/gitpod-sdk-python/issues/26)) ([e4040d1](https://github.com/gitpod-io/gitpod-sdk-python/commit/e4040d15067dea4ce6eb57742e6857bd8c227c4b))
* **internal:** update client tests ([#32](https://github.com/gitpod-io/gitpod-sdk-python/issues/32)) ([47d7150](https://github.com/gitpod-io/gitpod-sdk-python/commit/47d715021c3ca29e930c5b9e928e2f4aeb201ecc))

## 0.1.0-alpha.2 (2025-02-12)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** manual updates ([#18](https://github.com/gitpod-io/gitpod-sdk-python/issues/18)) ([06b6d24](https://github.com/gitpod-io/gitpod-sdk-python/commit/06b6d240835591bac5f684eb4c5b948ad16c831a))
* **api:** manual updates ([#19](https://github.com/gitpod-io/gitpod-sdk-python/issues/19)) ([ad9f662](https://github.com/gitpod-io/gitpod-sdk-python/commit/ad9f6629f8ba9b829299c3e43efea320f80e9d62))
* **api:** manual updates ([#20](https://github.com/gitpod-io/gitpod-sdk-python/issues/20)) ([1a90a1b](https://github.com/gitpod-io/gitpod-sdk-python/commit/1a90a1bf843979c5ca263e88f36afd04265e7137))


### Chores

* update SDK settings ([#16](https://github.com/gitpod-io/gitpod-sdk-python/issues/16)) ([daa1308](https://github.com/gitpod-io/gitpod-sdk-python/commit/daa13087a8e0e3678365e5ef51cd3db2f4737327))

## 0.1.0-alpha.1 (2025-02-11)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/gitpod-io/gitpod-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** add events streaming ([1d7a848](https://github.com/gitpod-io/gitpod-sdk-python/commit/1d7a848908ba3cb5c527bc6253c19e5a84a28b18))
* **api:** dedupe paginations ([75dc8c4](https://github.com/gitpod-io/gitpod-sdk-python/commit/75dc8c43b9ef8453cac3d9f18aafaa5deffca48f))
* **api:** fix pagination field names ([af22da1](https://github.com/gitpod-io/gitpod-sdk-python/commit/af22da11015915a96f68f74851abc7442fc4a0bf))
* **api:** manual updates ([0f00366](https://github.com/gitpod-io/gitpod-sdk-python/commit/0f00366da2833f31a9f298ac6c2ae980c1a6db99))
* **api:** manual updates ([4d19977](https://github.com/gitpod-io/gitpod-sdk-python/commit/4d199779647d6fafb2a1a26872b5a72c4b3378b6))
* **api:** pagination config ([c407e2e](https://github.com/gitpod-io/gitpod-sdk-python/commit/c407e2eaadda4d1ccbba6065235eac03a2332c48))
* **api:** properly produce empty request bodies ([#4](https://github.com/gitpod-io/gitpod-sdk-python/issues/4)) ([157b351](https://github.com/gitpod-io/gitpod-sdk-python/commit/157b35194ee33d9e83277e5b559a214c21e37531))
* **api:** try to fix updateenvironmentrequest ([#8](https://github.com/gitpod-io/gitpod-sdk-python/issues/8)) ([4d8e7c2](https://github.com/gitpod-io/gitpod-sdk-python/commit/4d8e7c207031edf11b3a3a9163f62b8e8d2f6576))
* **api:** update to latest changes ([#10](https://github.com/gitpod-io/gitpod-sdk-python/issues/10)) ([7822990](https://github.com/gitpod-io/gitpod-sdk-python/commit/7822990e687b35793e921b43aaa5cc73e101ae0f))
* **api:** update via SDK Studio ([3e66ecc](https://github.com/gitpod-io/gitpod-sdk-python/commit/3e66ecc1e5b3f7495b143f9fb31df85d24b871c6))
* **api:** update via SDK Studio ([66db733](https://github.com/gitpod-io/gitpod-sdk-python/commit/66db73366f6edaf7f0b21c1a88ec230b8650423d))
* **api:** update via SDK Studio ([d20eaba](https://github.com/gitpod-io/gitpod-sdk-python/commit/d20eaba8a2034c60b7957e74b1b060305102a520))
* **api:** update via SDK Studio ([b418dbe](https://github.com/gitpod-io/gitpod-sdk-python/commit/b418dbed6ce6c7e3a6eeee211f3391342cdc9d51))
* **api:** update via SDK Studio ([06c4b10](https://github.com/gitpod-io/gitpod-sdk-python/commit/06c4b10fff0b115550b0ab3a5fa106348d3868d4))
* **api:** update via SDK Studio ([5b25656](https://github.com/gitpod-io/gitpod-sdk-python/commit/5b2565694ed495e564f948078c02dd46efe8fadf))
* **api:** update via SDK Studio ([ea67c8c](https://github.com/gitpod-io/gitpod-sdk-python/commit/ea67c8c3e4ed067a049153a6807051bdf6f64cff))
* **api:** update via SDK Studio ([974fb63](https://github.com/gitpod-io/gitpod-sdk-python/commit/974fb635622cc790b134afa0e374e27951ab59b4))
* **api:** update via SDK Studio ([4e32701](https://github.com/gitpod-io/gitpod-sdk-python/commit/4e3270181d05a023bec2afc835dea83fcdcec3b2))
* **api:** update via SDK Studio ([f8ce60d](https://github.com/gitpod-io/gitpod-sdk-python/commit/f8ce60dbadb28a8d29184ac561f5c0608e23e5a0))
* **api:** update via SDK Studio ([87524c3](https://github.com/gitpod-io/gitpod-sdk-python/commit/87524c331c989fa4debc93bede3e16659f94ec62))
* **api:** update via SDK Studio ([2ac41b3](https://github.com/gitpod-io/gitpod-sdk-python/commit/2ac41b3c8889105bd7d5c9a052468646bd670252))
* **api:** update via SDK Studio ([7b2f2cf](https://github.com/gitpod-io/gitpod-sdk-python/commit/7b2f2cf872b573c4945ab7eb83e1011dcd082f06))
* **api:** update via SDK Studio ([c8930ae](https://github.com/gitpod-io/gitpod-sdk-python/commit/c8930ae28eb3d89dd32ca1db15d1bd4bd0423498))
* **api:** update via SDK Studio ([e42265e](https://github.com/gitpod-io/gitpod-sdk-python/commit/e42265e20f8fb254f4ea31f4f868de669dd31475))
* **api:** update via SDK Studio ([dd8ecd8](https://github.com/gitpod-io/gitpod-sdk-python/commit/dd8ecd84a27bb9c9701c269e05300a7d2d4e5708))
* **api:** update via SDK Studio ([8d5f640](https://github.com/gitpod-io/gitpod-sdk-python/commit/8d5f640dd221b455794a8cf40b2071af0467d3f5))
* **api:** update via SDK Studio ([e27af94](https://github.com/gitpod-io/gitpod-sdk-python/commit/e27af94de0c010b0970f3badad10ee35034dfe1d))
* **api:** update via SDK Studio ([48a5274](https://github.com/gitpod-io/gitpod-sdk-python/commit/48a5274bbc3678b4a0cc74679efa9884acb258df))
* **api:** update via SDK Studio ([2139387](https://github.com/gitpod-io/gitpod-sdk-python/commit/2139387ad0c36be18b31a0f3446c39c974637520))
* **api:** update via SDK Studio ([afa5045](https://github.com/gitpod-io/gitpod-sdk-python/commit/afa504592f2b73d450dfc7e9bd074fa22c23be7e))
* **client:** send `X-Stainless-Read-Timeout` header ([#6](https://github.com/gitpod-io/gitpod-sdk-python/issues/6)) ([682f05a](https://github.com/gitpod-io/gitpod-sdk-python/commit/682f05ae477692948c35e34666efa39110431020))
* **jsonl:** add .close() method ([#11](https://github.com/gitpod-io/gitpod-sdk-python/issues/11)) ([7d017fd](https://github.com/gitpod-io/gitpod-sdk-python/commit/7d017fdfa06fbc5297a5e58f9b110de5d8d7e7d0))
* pagination responses ([d009d64](https://github.com/gitpod-io/gitpod-sdk-python/commit/d009d64229f53e4f271799d273bbbae26fb3520b))


### Bug Fixes

* **api:** better support union schemas with common properties ([ad416b2](https://github.com/gitpod-io/gitpod-sdk-python/commit/ad416b216575ab7c015ab984dd94a72b240ad467))
* **client:** compat with new httpx 0.28.0 release ([abc0621](https://github.com/gitpod-io/gitpod-sdk-python/commit/abc0621222e659f182967b3ca147280f244e1fc4))
* **client:** only call .close() when needed ([bbb6747](https://github.com/gitpod-io/gitpod-sdk-python/commit/bbb6747ad4d09e9066cda67947fea40937d89bd2))
* correctly handle deserialising `cls` fields ([df55d8a](https://github.com/gitpod-io/gitpod-sdk-python/commit/df55d8a1decd0514c24033b9f2615616a1ae2292))
* **jsonl:** lower chunk size ([#12](https://github.com/gitpod-io/gitpod-sdk-python/issues/12)) ([f07eb3f](https://github.com/gitpod-io/gitpod-sdk-python/commit/f07eb3fee38d93d8ac2955f2846f8dd6ca74a5cc))
* pagination example ([8ddfb41](https://github.com/gitpod-io/gitpod-sdk-python/commit/8ddfb41ab1b872e2d8535194801826e88e7dee08))
* pagination response ([ba50863](https://github.com/gitpod-io/gitpod-sdk-python/commit/ba50863a1b9e11dcaafa657475081147f2fefd23))
* **tests:** disable mock tests ([#5](https://github.com/gitpod-io/gitpod-sdk-python/issues/5)) ([96537af](https://github.com/gitpod-io/gitpod-sdk-python/commit/96537af8e3e02ea3b043d5e1433df56344bfdea8))
* **tests:** disable test mocks ([#3](https://github.com/gitpod-io/gitpod-sdk-python/issues/3)) ([9a6b2e8](https://github.com/gitpod-io/gitpod-sdk-python/commit/9a6b2e8c7693b6de6cc15efcd6ea9594f90e291f))
* **tests:** make test_get_platform less flaky ([51968d4](https://github.com/gitpod-io/gitpod-sdk-python/commit/51968d4b351b54b5b402d8a77b37249205fe3681))


### Chores

* add missing isclass check ([ff7cbaa](https://github.com/gitpod-io/gitpod-sdk-python/commit/ff7cbaa4807baf6951a6317880ab894949129e85))
* go live ([#1](https://github.com/gitpod-io/gitpod-sdk-python/issues/1)) ([c9a1a30](https://github.com/gitpod-io/gitpod-sdk-python/commit/c9a1a30529fdd39494b65ddfaa724c255fa52888))
* go live ([#14](https://github.com/gitpod-io/gitpod-sdk-python/issues/14)) ([566fc35](https://github.com/gitpod-io/gitpod-sdk-python/commit/566fc3518fc2448b8d98b5f1f24f668c91343a7e))
* **internal:** avoid pytest-asyncio deprecation warning ([3c00c53](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c00c53a00ff67157829da89bbbaceae142a411e))
* **internal:** bump httpx dependency ([e160bd9](https://github.com/gitpod-io/gitpod-sdk-python/commit/e160bd9a691017994b8704cca5eaaef0d0344940))
* **internal:** bump pydantic dependency ([5ce555b](https://github.com/gitpod-io/gitpod-sdk-python/commit/5ce555ba5ccdfa37a62c891e46a1758e1445369c))
* **internal:** bump pyright ([aba3b34](https://github.com/gitpod-io/gitpod-sdk-python/commit/aba3b34b382753596f0e3bbc211221b307d2d32c))
* **internal:** change default timeout to an int ([6430f4c](https://github.com/gitpod-io/gitpod-sdk-python/commit/6430f4cde5fb665c32501880ff06127b348e8b31))
* **internal:** codegen related update ([ec5eb7e](https://github.com/gitpod-io/gitpod-sdk-python/commit/ec5eb7e1ab7ce34c1f359300fdc1354e1d5cf549))
* **internal:** codegen related update ([497ae18](https://github.com/gitpod-io/gitpod-sdk-python/commit/497ae18d5624499a7c907f4689a8879b7c1d40b1))
* **internal:** codegen related update ([c9288d5](https://github.com/gitpod-io/gitpod-sdk-python/commit/c9288d535936274a7927b2bb2bf7e424e5b1e8b4))
* **internal:** codegen related update ([cb8475b](https://github.com/gitpod-io/gitpod-sdk-python/commit/cb8475b8084ade988b2861b636a432d45fb3b2ff))
* **internal:** codegen related update ([26b774b](https://github.com/gitpod-io/gitpod-sdk-python/commit/26b774b422be3b8f51ab25facff1c75c89257991))
* **internal:** codegen related update ([0f3b621](https://github.com/gitpod-io/gitpod-sdk-python/commit/0f3b6216e5c5fe1155fa8ae28fb8a81c65421267))
* **internal:** codegen related update ([0dab9d3](https://github.com/gitpod-io/gitpod-sdk-python/commit/0dab9d38924656bf9c2132a320d1233bc61e696a))
* **internal:** codegen related update ([838ff11](https://github.com/gitpod-io/gitpod-sdk-python/commit/838ff11b1d62ddc7148953e73262a35e1ec575ec))
* **internal:** codegen related update ([fafa29d](https://github.com/gitpod-io/gitpod-sdk-python/commit/fafa29d268068e422e5b774eacdd2faedbe32f39))
* **internal:** codegen related update ([80c8bbf](https://github.com/gitpod-io/gitpod-sdk-python/commit/80c8bbfa9f757e97878d336cd9cd7babe5d52d6b))
* **internal:** codegen related update ([36c6d5e](https://github.com/gitpod-io/gitpod-sdk-python/commit/36c6d5eb17f40adb63a29f22d89afa8eca9c0677))
* **internal:** exclude mypy from running on tests ([cae2176](https://github.com/gitpod-io/gitpod-sdk-python/commit/cae2176e0a99d1094f797fb49baab2435c04d5f6))
* **internal:** fix compat model_dump method when warnings are passed ([ee87f96](https://github.com/gitpod-io/gitpod-sdk-python/commit/ee87f963bab5e9ac07b3a9fb4c40f46ca3a07613))
* **internal:** fix some typos ([c0f7e58](https://github.com/gitpod-io/gitpod-sdk-python/commit/c0f7e58307c3602499e72354aee6d2ada1e15528))
* **internal:** fix type traversing dictionary params ([#7](https://github.com/gitpod-io/gitpod-sdk-python/issues/7)) ([86cea9d](https://github.com/gitpod-io/gitpod-sdk-python/commit/86cea9dcf4c25a5787023bb9ab378ac1b90e9b7c))
* **internal:** minor formatting changes ([2273048](https://github.com/gitpod-io/gitpod-sdk-python/commit/2273048b7dbc282f31edf563d56ff8dd223969d8))
* **internal:** minor type handling changes ([#9](https://github.com/gitpod-io/gitpod-sdk-python/issues/9)) ([c10beb0](https://github.com/gitpod-io/gitpod-sdk-python/commit/c10beb0e2369438df39099e48fe7f0a0d4bcace5))
* **internal:** remove some duplicated imports ([8e6cc74](https://github.com/gitpod-io/gitpod-sdk-python/commit/8e6cc74d2e16297d05cd9cc233e4d79fdff64930))
* **internal:** update examples ([d652f4e](https://github.com/gitpod-io/gitpod-sdk-python/commit/d652f4e1ab70a731eff04beb3ff0f7c471dbcacf))
* **internal:** updated imports ([d31547b](https://github.com/gitpod-io/gitpod-sdk-python/commit/d31547b97db1baea0383ecb8a86e65270a093b77))
* make the `Omit` type public ([cf43176](https://github.com/gitpod-io/gitpod-sdk-python/commit/cf4317618f0cc177f812781d62bd454afa279f45))
* rebuild project due to codegen change ([4c930a5](https://github.com/gitpod-io/gitpod-sdk-python/commit/4c930a5227bbec3f5a3d378ababf01ae8d4cedb3))
* rebuild project due to codegen change ([b7129db](https://github.com/gitpod-io/gitpod-sdk-python/commit/b7129db829b29adc2fbcf0eebdfc9f97e80d74c6))
* rebuild project due to codegen change ([56f37cb](https://github.com/gitpod-io/gitpod-sdk-python/commit/56f37cb299889d38a458cacc659c21df8bf14fbe))
* rebuild project due to codegen change ([710a64b](https://github.com/gitpod-io/gitpod-sdk-python/commit/710a64bcff5107c7180c9c994594c30a65e182cb))
* remove now unused `cached-property` dep ([b66de02](https://github.com/gitpod-io/gitpod-sdk-python/commit/b66de02aeb1dfe216c3c6f4687db973de79f03d2))
* security config ([3c91d8f](https://github.com/gitpod-io/gitpod-sdk-python/commit/3c91d8f00626733cdfb925c0382b994f287b8c33))


### Documentation

* add info log level to readme ([aebe445](https://github.com/gitpod-io/gitpod-sdk-python/commit/aebe445be3e15f9773dad03ee9b3f565f3c7273b))
* fix typos ([35edab0](https://github.com/gitpod-io/gitpod-sdk-python/commit/35edab0b4da50551371b866f4a24a5c520fa9264))
* **raw responses:** fix duplicate `the` ([5d59373](https://github.com/gitpod-io/gitpod-sdk-python/commit/5d5937373485b2a0293d9ebd0ca949d9ed8da26f))
* **readme:** example snippet for client context manager ([b8180b3](https://github.com/gitpod-io/gitpod-sdk-python/commit/b8180b3266fe57a68e3e72af355bb7cc898b8bf2))
* **readme:** fix http client proxies example ([079665c](https://github.com/gitpod-io/gitpod-sdk-python/commit/079665c9ce58df2e2f7c77cb6b610fdb0dc62c43))
