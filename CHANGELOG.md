# Changelog

## [0.3.0](https://github.com/masakaya/python-uv-project/compare/v0.2.1...v0.3.0) (2025-11-21)


### Features

* Add automatic promotion PRs (main → staging → production) ([#7](https://github.com/masakaya/python-uv-project/issues/7)) ([b139909](https://github.com/masakaya/python-uv-project/commit/b139909d113e65610b48610e7944de4d66b475e0))
* Add coverage comment to PR ([#6](https://github.com/masakaya/python-uv-project/issues/6)) ([528d3a5](https://github.com/masakaya/python-uv-project/commit/528d3a5a892e9e3f42e56dc3810be2b5d5d24add))
* add GitHub Actions version management to Renovate ([#36](https://github.com/masakaya/python-uv-project/issues/36)) ([cc35b88](https://github.com/masakaya/python-uv-project/commit/cc35b8866a11c044085702855e61b08c260f2eb3))
* add PR and Issue templates ([#37](https://github.com/masakaya/python-uv-project/issues/37)) ([141d734](https://github.com/masakaya/python-uv-project/commit/141d734d51e34a088d7660fcc4a0885f6193cb0b))
* add security and docstring linting rules to ruff ([#34](https://github.com/masakaya/python-uv-project/issues/34)) ([f35cb39](https://github.com/masakaya/python-uv-project/commit/f35cb393d1e064e2ebf9b822ace7f4e198345bf5))
* replace promotion workflow with git-pr-release ([d477e9a](https://github.com/masakaya/python-uv-project/commit/d477e9a37b8dcbde0ecdda4089ff6c354410b2ee))
* replace promotion workflow with git-pr-release ([2a2c7ee](https://github.com/masakaya/python-uv-project/commit/2a2c7ee62427915eaf592b3b76eae0200327185a))
* Setup modern Python project template ([#2](https://github.com/masakaya/python-uv-project/issues/2)) ([de98778](https://github.com/masakaya/python-uv-project/commit/de98778cd920bdfdba0d8acfa24213e4976334ba))
* Setup Renovate for automatic dependency updates ([#3](https://github.com/masakaya/python-uv-project/issues/3)) ([dbfaaf1](https://github.com/masakaya/python-uv-project/commit/dbfaaf1047f0da08d07f37deea2e42a745666689))
* test promotion workflow ([#45](https://github.com/masakaya/python-uv-project/issues/45)) ([f97620b](https://github.com/masakaya/python-uv-project/commit/f97620b5400928d55f5f39521e65a48d76d2f019))
* test promotion workflow v2 ([#48](https://github.com/masakaya/python-uv-project/issues/48)) ([b2dadb4](https://github.com/masakaya/python-uv-project/commit/b2dadb41e4d674c9a721cd446c07e8c8b8c2aed4))


### Bug Fixes

* add auto-resolution for workflow file conflicts ([#21](https://github.com/masakaya/python-uv-project/issues/21)) ([d98333d](https://github.com/masakaya/python-uv-project/commit/d98333de8ff0c1f0b832a767b98c874081d3167e))
* add conflict auto-resolution before git-pr-release ([#47](https://github.com/masakaya/python-uv-project/issues/47)) ([c90f0c5](https://github.com/masakaya/python-uv-project/commit/c90f0c52dd35cfacc0f821fc9715f79edaafbd95))
* auto-resolve ALL conflicts in promotion workflows ([#28](https://github.com/masakaya/python-uv-project/issues/28)) ([05b7816](https://github.com/masakaya/python-uv-project/commit/05b7816b3ee34a5bde98059357cbffe1b62db88b))
* auto-resolve manifest.json conflicts in promotion workflows ([#18](https://github.com/masakaya/python-uv-project/issues/18)) ([80967f0](https://github.com/masakaya/python-uv-project/commit/80967f0bdd395bbf0a86dddc85a5d71a7dc1a4d9))
* change filter-mode to diff_context for reviewdog ([cfced61](https://github.com/masakaya/python-uv-project/commit/cfced619a696bb278480bf73ddd649995305f0e6))
* configure release-please for production branch ([#26](https://github.com/masakaya/python-uv-project/issues/26)) ([04adcce](https://github.com/masakaya/python-uv-project/commit/04adcce7e1d44c085922841690439583cfc7e36b))
* consolidate promotion PRs into single PR per target ([c5962c2](https://github.com/masakaya/python-uv-project/commit/c5962c29a3d1dccbf59cbb1f14e007d1a15cec56))
* consolidate promotion PRs into single PR per target ([75417a3](https://github.com/masakaya/python-uv-project/commit/75417a3325dbaed68a2f4f56724171fd637e7e1f))
* correct secrets conditional expression syntax ([#9](https://github.com/masakaya/python-uv-project/issues/9)) ([5d0b5b4](https://github.com/masakaya/python-uv-project/commit/5d0b5b4ba54be7ce282b7baa69b2760a93c9777a))
* correct test workflow codecov configuration ([#8](https://github.com/masakaya/python-uv-project/issues/8)) ([7314d39](https://github.com/masakaya/python-uv-project/commit/7314d39364c897c1bb534a646dd361d37a2f9f2d))
* correct YAML syntax in promotion workflow commit messages ([#19](https://github.com/masakaya/python-uv-project/issues/19)) ([4fee4b2](https://github.com/masakaya/python-uv-project/commit/4fee4b20ec25419141b3f60ef1ff5f365fad5eb2))
* **mypy:** use errorformat instead of -f=mypy ([de0085c](https://github.com/masakaya/python-uv-project/commit/de0085c827f082b0294eabf060a0e09c4a6afc43))
* **ruff:** add --output-format=concise for reviewdog ([adfd401](https://github.com/masakaya/python-uv-project/commit/adfd401a31b4a1f5c672f02d1141defbbaf8ba0f))
* **ruff:** use errorformat instead of unsupported -f=ruff ([540913b](https://github.com/masakaya/python-uv-project/commit/540913b5db347435ea02c5960a583db29f482e3e))
* **ruff:** use github output format for reviewdog ([5dc7c11](https://github.com/masakaya/python-uv-project/commit/5dc7c11f18b5e7cf0d540dfadf4a5f4eea8d6da3))
* simplify codecov conditional to avoid expression syntax error ([#12](https://github.com/masakaya/python-uv-project/issues/12)) ([9b0e5e4](https://github.com/masakaya/python-uv-project/commit/9b0e5e4271f0b2dadc1822eca794f94c93622d41))
* simplify promotion workflow and fix template ([#49](https://github.com/masakaya/python-uv-project/issues/49)) ([920f0e5](https://github.com/masakaya/python-uv-project/commit/920f0e5990a0fe5776dcade897130362eac19f54))
* use environment variable for codecov conditional ([#13](https://github.com/masakaya/python-uv-project/issues/13)) ([bf8f029](https://github.com/masakaya/python-uv-project/commit/bf8f02932b4720fa6c0b89a2cf1004470b3ffa3b))
* wrap secrets reference in expression syntax ([#11](https://github.com/masakaya/python-uv-project/issues/11)) ([5f6d992](https://github.com/masakaya/python-uv-project/commit/5f6d99268cb008039263965af37deac892876830))


### Miscellaneous

* **main:** release python-uv-project 0.2.0 ([#15](https://github.com/masakaya/python-uv-project/issues/15)) ([20e7bad](https://github.com/masakaya/python-uv-project/commit/20e7bad1b2816331b928403988da1e3466353bff))
* **main:** release python-uv-project 0.2.1 ([#24](https://github.com/masakaya/python-uv-project/issues/24)) ([e31ebd1](https://github.com/masakaya/python-uv-project/commit/e31ebd1cde96d30bef10c9ebfacc62b60ed49046))
* trigger promotion workflow to sync latest changes ([a46dcf1](https://github.com/masakaya/python-uv-project/commit/a46dcf1219b72402cfc76422d271050afb709661))
* trigger test workflow to verify fix ([b959845](https://github.com/masakaya/python-uv-project/commit/b959845b1793ef8363f6ef8323c0ce4030931aec))


### Documentation

* add branch naming convention to Claude.md ([#42](https://github.com/masakaya/python-uv-project/issues/42)) ([01ea15c](https://github.com/masakaya/python-uv-project/commit/01ea15c3a8447ced5c69eae0334e233be65e4209))
* update README with branch promotion workflow ([#32](https://github.com/masakaya/python-uv-project/issues/32)) ([a9150e3](https://github.com/masakaya/python-uv-project/commit/a9150e3a615def642c59fc8e178f11bda53b9e41))

## [0.2.1](https://github.com/masakaya/python-uv-project/compare/python-uv-project-v0.2.0...python-uv-project-v0.2.1) (2025-11-21)


### Bug Fixes

* add auto-resolution for workflow file conflicts ([#21](https://github.com/masakaya/python-uv-project/issues/21)) ([d98333d](https://github.com/masakaya/python-uv-project/commit/d98333de8ff0c1f0b832a767b98c874081d3167e))
* auto-resolve manifest.json conflicts in promotion workflows ([#18](https://github.com/masakaya/python-uv-project/issues/18)) ([80967f0](https://github.com/masakaya/python-uv-project/commit/80967f0bdd395bbf0a86dddc85a5d71a7dc1a4d9))
* correct YAML syntax in promotion workflow commit messages ([#19](https://github.com/masakaya/python-uv-project/issues/19)) ([4fee4b2](https://github.com/masakaya/python-uv-project/commit/4fee4b20ec25419141b3f60ef1ff5f365fad5eb2))

## [0.2.0](https://github.com/masakaya/python-uv-project/compare/python-uv-project-v0.1.0...python-uv-project-v0.2.0) (2025-11-20)


### Features

* Add automatic promotion PRs (main → staging → production) ([#7](https://github.com/masakaya/python-uv-project/issues/7)) ([b139909](https://github.com/masakaya/python-uv-project/commit/b139909d113e65610b48610e7944de4d66b475e0))
* Add coverage comment to PR ([#6](https://github.com/masakaya/python-uv-project/issues/6)) ([528d3a5](https://github.com/masakaya/python-uv-project/commit/528d3a5a892e9e3f42e56dc3810be2b5d5d24add))
* Setup modern Python project template ([#2](https://github.com/masakaya/python-uv-project/issues/2)) ([de98778](https://github.com/masakaya/python-uv-project/commit/de98778cd920bdfdba0d8acfa24213e4976334ba))
* Setup Renovate for automatic dependency updates ([#3](https://github.com/masakaya/python-uv-project/issues/3)) ([dbfaaf1](https://github.com/masakaya/python-uv-project/commit/dbfaaf1047f0da08d07f37deea2e42a745666689))


### Bug Fixes

* change filter-mode to diff_context for reviewdog ([cfced61](https://github.com/masakaya/python-uv-project/commit/cfced619a696bb278480bf73ddd649995305f0e6))
* correct secrets conditional expression syntax ([#9](https://github.com/masakaya/python-uv-project/issues/9)) ([5d0b5b4](https://github.com/masakaya/python-uv-project/commit/5d0b5b4ba54be7ce282b7baa69b2760a93c9777a))
* correct test workflow codecov configuration ([#8](https://github.com/masakaya/python-uv-project/issues/8)) ([7314d39](https://github.com/masakaya/python-uv-project/commit/7314d39364c897c1bb534a646dd361d37a2f9f2d))
* **mypy:** use errorformat instead of -f=mypy ([de0085c](https://github.com/masakaya/python-uv-project/commit/de0085c827f082b0294eabf060a0e09c4a6afc43))
* **ruff:** add --output-format=concise for reviewdog ([adfd401](https://github.com/masakaya/python-uv-project/commit/adfd401a31b4a1f5c672f02d1141defbbaf8ba0f))
* **ruff:** use errorformat instead of unsupported -f=ruff ([540913b](https://github.com/masakaya/python-uv-project/commit/540913b5db347435ea02c5960a583db29f482e3e))
* **ruff:** use github output format for reviewdog ([5dc7c11](https://github.com/masakaya/python-uv-project/commit/5dc7c11f18b5e7cf0d540dfadf4a5f4eea8d6da3))
* simplify codecov conditional to avoid expression syntax error ([#12](https://github.com/masakaya/python-uv-project/issues/12)) ([9b0e5e4](https://github.com/masakaya/python-uv-project/commit/9b0e5e4271f0b2dadc1822eca794f94c93622d41))
* use environment variable for codecov conditional ([#13](https://github.com/masakaya/python-uv-project/issues/13)) ([bf8f029](https://github.com/masakaya/python-uv-project/commit/bf8f02932b4720fa6c0b89a2cf1004470b3ffa3b))
* wrap secrets reference in expression syntax ([#11](https://github.com/masakaya/python-uv-project/issues/11)) ([5f6d992](https://github.com/masakaya/python-uv-project/commit/5f6d99268cb008039263965af37deac892876830))


### Miscellaneous

* trigger test workflow to verify fix ([b959845](https://github.com/masakaya/python-uv-project/commit/b959845b1793ef8363f6ef8323c0ce4030931aec))
