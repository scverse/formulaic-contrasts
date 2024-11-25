from collections.abc import Sequence

import pandas as pd
import pytest

from formulaic_contrasts import FormulaicContrasts


@pytest.fixture
def MockModel():
    class _MockModel(FormulaicContrasts):
        def _check_counts(self) -> None:
            pass

        def fit(self, **kwargs) -> None:
            pass

        def _test_single_contrast(self, contrast: Sequence[float], **kwargs) -> pd.DataFrame:
            pass

    return _MockModel


@pytest.mark.parametrize(
    "formula,cond_kwargs,expected_contrast",
    [
        # single variable
        ["~ condition", {}, [1, 0]],
        ["~ condition", {"condition": "A"}, [1, 0]],
        ["~ condition", {"condition": "B"}, [1, 1]],
        ["~ condition", {"condition": "42"}, ValueError],  # non-existant category
        # no-intercept models
        ["~ 0 + condition", {"condition": "A"}, [1, 0]],
        ["~ 0 + condition", {"condition": "B"}, [0, 1]],
        # Different way of specifying dummy coding
        ["~ donor", {"donor": "D0"}, [1, 0, 0, 0]],
        ["~ C(donor)", {"donor": "D0"}, [1, 0, 0, 0]],
        ["~ C(donor, contr.treatment(base='D2'))", {"donor": "D2"}, [1, 0, 0, 0]],
        ["~ C(donor, contr.treatment(base='D2'))", {"donor": "D0"}, [1, 1, 0, 0]],
        # Handle continuous covariates
        ["~ donor + continuous", {"donor": "D1"}, [1, 1, 0, 0, 0]],
        ["~ donor + np.log1p(continuous)", {"donor": "D1"}, [1, 1, 0, 0, 0]],
        ["~ donor + continuous + np.log1p(continuous)", {"donor": "D0"}, [1, 0, 0, 0, 0, 0]],
        # Nonsense models repeating the same variable, which are nonetheless allowed by formulaic
        ["~ donor + C(donor)", {"donor": "D1"}, [1, 1, 0, 0, 1, 0, 0]],
        ["~ donor + C(donor, contr.treatment(base='D2'))", {"donor": "D0"}, [1, 0, 0, 0, 1, 0, 0]],
        [
            "~ condition + donor + C(donor, contr.treatment(base='D2'))",
            {"condition": "A"},
            ValueError,
        ],  # donor base category can't be resolved because it's ambiguous -> ValueError
        # Sum2zero coding
        ["~ C(donor, contr.sum)", {"donor": "D0"}, [1, 1, 0, 0]],
        ["~ C(donor, contr.sum)", {"donor": "D3"}, [1, -1, -1, -1]],
        # Multiple categorical variables
        ["~ condition + donor", {"condition": "A"}, [1, 0, 0, 0, 0]],
        ["~ condition + donor", {"donor": "D2"}, [1, 0, 0, 1, 0]],
        ["~ condition + donor", {"condition": "B", "donor": "D2"}, [1, 1, 0, 1, 0]],
        ["~ 0 + condition + donor", {"donor": "D1"}, [0, 0, 1, 0, 0]],
        # Interaction terms
        ["~ condition * donor", {"condition": "A"}, [1, 0, 0, 0, 0, 0, 0, 0]],
        ["~ condition + donor + condition:donor", {"condition": "A"}, [1, 0, 0, 0, 0, 0, 0, 0]],
        ["~ condition * donor", {"condition": "B", "donor": "D2"}, [1, 1, 0, 1, 0, 0, 1, 0]],
        ["~ condition * C(donor, contr.treatment(base='D2'))", {"condition": "A"}, [1, 0, 0, 0, 0, 0, 0, 0]],
        [
            "~ condition * C(donor, contr.treatment(base='D2'))",
            {"condition": "B", "donor": "D0"},
            [1, 1, 1, 0, 0, 1, 0, 0],
        ],
        [
            "~ condition:donor",
            {"condition": "A"},
            ValueError,
        ],  # Can't automatically resolve base category, because Formulaic builds a reduced-rank and full-rank factor internally
        ["~ condition:donor", {"condition": "A", "donor": "D1"}, [1, 1, 0, 0, 0, 0, 0, 0]],
        ["~ condition:C(donor)", {"condition": "A", "donor": "D1"}, [1, 1, 0, 0, 0, 0, 0, 0]],
    ],
)
def test_model_cond(test_dataframe, MockModel, formula, cond_kwargs, expected_contrast):
    mod = MockModel(test_dataframe, formula)
    if isinstance(expected_contrast, type):
        with pytest.raises(expected_contrast):
            mod.cond(**cond_kwargs)
    else:
        actual_contrast = mod.cond(**cond_kwargs)
        assert actual_contrast.tolist() == expected_contrast
        assert actual_contrast.index.tolist() == mod.design.columns.tolist()
