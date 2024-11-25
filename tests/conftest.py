import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def test_dataframe():
    n_obs = 80
    n_donors = n_obs // 4
    rng = np.random.default_rng(9)  # make tests deterministic
    return pd.DataFrame(
        {
            "condition": ["A", "B"] * (n_obs // 2),
            "donor": sum(([f"D{i}"] * n_donors for i in range(n_obs // n_donors)), []),
            "other": (["X"] * (n_obs // 4)) + (["Y"] * ((3 * n_obs) // 4)),
            "pairing": sum(([str(i), str(i)] for i in range(n_obs // 2)), []),
            "continuous": [rng.uniform(0, 1) * 4000 for _ in range(n_obs)],
        },
    )
