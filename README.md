# formulaic-contrasts

[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]
[![codecov.io][badge-codecov]][link-codecov]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/scverse/formulaic-contrasts/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/formulaic-contrasts
[badge-codecov]: https://codecov.io/github/scverse/formulaic-contrasts/coverage.svg?branch=main
[link-codecov]: https://codecov.io/gh/scverse/formulaic-contrasts/branch/main

Build arbitrary contrasts for models defined with formulaic.

## Getting started

Please refer to the [documentation][]. As a developer seeking to use `formulaic-contrasts` with your model, you'll find
the [API documentation][] and the tutorial [Usage in custom model][] useful. If you are a user who wants to understand
how to build contrasts for a model, the [building contrasts][] tutorial is for you!

## Installation

Typically, you don't install `formulaic-contrasts` directly, but obtain it as a dependency of
another model. As a developer, you can obtain it from PyPI or GitHub:

There are several alternative options to install formulaic-contrasts:

1. Install the latest release of `formulaic-contrasts` from [PyPI][]:

```bash
pip install formulaic-contrasts
```

2. Install the latest development version:

```bash
pip install git+https://github.com/scverse/formulaic-contrasts.git@main
```

`Formulaic-contrasts` depends on Python 3.10 or later.

## Release notes

See the [changelog][].

## Contact

For questions and help requests, you can reach out in the [scverse discourse][].
If you found a bug, please use the [issue tracker][].

## Credits

The `cond()` function for building contrasts has been devised by [@const-ae](https://github.com/const-ae) for his R package [glmGamPoi](https://bioconductor.org/packages/release/bioc/html/glmGamPoi.html). A [prototype](https://github.com/scverse/multi-condition-comparisions) of the Python implementation has been built at the [scverse hackathon in Cambridge, UK in Nov 2023](https://scverse.org/events/2023_11_hackathon/) by [@grst](https://github.com/grst), [@const-ae](https://github.com/const-ae) and [@BorisMuzellec](https://github.com/BorisMuzellec). The production version in this package has been implemented by [@grst](https://github.com/grst).

[mambaforge]: https://github.com/conda-forge/miniforge#mambaforge
[scverse discourse]: https://discourse.scverse.org/
[issue tracker]: https://github.com/scverse/formulaic-contrasts/issues
[tests]: https://github.com/scverse/formulaic-contrasts/actions/workflows/test.yml
[documentation]: https://formulaic-contrasts.readthedocs.io
[changelog]: https://formulaic-contrasts.readthedocs.io/en/latest/changelog.html
[api documentation]: https://formulaic-contrasts.readthedocs.io/en/latest/api.html
[usage in custom model]: https://formulaic-contrasts.readthedocs.io/en/latest/model_usage.html
[building contrasts]: https://formulaic-contrasts.readthedocs.io/en/latest/contrasts.html
[pypi]: https://pypi.org/project/formulaic-contrasts
