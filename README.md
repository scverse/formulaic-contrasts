# formulaic-contrasts

[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/scverse/formulaic-contrasts/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/formulaic-contrasts

Build contrasts for models defined with formulaic

## Getting started

Please refer to the [documentation][],
in particular, the [API documentation][].

## Installation

You need to have Python 3.10 or newer installed on your system.
If you don't have Python installed, we recommend installing [Mambaforge][].

There are several alternative options to install formulaic-contrasts:

1. Install the latest release of `formulaic-contrasts` from [PyPI][]:

```bash
pip install formulaic-contrasts
```

2. Install the latest development version:

```bash
pip install git+https://github.com/scverse/formulaic-contrasts.git@main
```

## Release notes

See the [changelog][].

## Contact

For questions and help requests, you can reach out in the [scverse discourse][].
If you found a bug, please use the [issue tracker][].

## Credits

The `cond()` function for building contrasts has been devised by @const-ae for his R package [glmGamPoi](https://bioconductor.org/packages/release/bioc/html/glmGamPoi.html). A [prototype](https://github.com/scverse/multi-condition-comparisions) of the Python implementation has been built at the [scverse hackathon in Cambridge, UK in Nov 2023](https://scverse.org/events/2023_11_hackathon/) by @grst, @const-ae and @BorisMuzellec. The production version in this package has been implemented by @grst.

[mambaforge]: https://github.com/conda-forge/miniforge#mambaforge
[scverse discourse]: https://discourse.scverse.org/
[issue tracker]: https://github.com/scverse/formulaic-contrasts/issues
[tests]: https://github.com/scverse/formulaic-contrasts/actions/workflows/test.yml
[documentation]: https://formulaic-contrasts.readthedocs.io
[changelog]: https://formulaic-contrasts.readthedocs.io/en/latest/changelog.html
[api documentation]: https://formulaic-contrasts.readthedocs.io/en/latest/api.html
[pypi]: https://pypi.org/project/formulaic-contrasts
