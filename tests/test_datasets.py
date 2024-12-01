import pytest

from formulaic_contrasts.datasets import treatment_response


@pytest.mark.parametrize("size,size_expected", [(80, 80), (90, ValueError), (160, 160)])
def test_treatment_response(size, size_expected):
    if isinstance(size_expected, type):
        with pytest.raises(size_expected):
            df = treatment_response(size)
    else:
        df = treatment_response(size)
        assert df.columns.tolist() == ["treatment", "response", "biomarker"]
        assert df.shape[0] == size_expected
