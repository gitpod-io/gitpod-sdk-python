# Changelog

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
