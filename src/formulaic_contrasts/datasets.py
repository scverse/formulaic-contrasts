import random

import pandas as pd


def treatment_response(size: int = 80, *, seed: int = 0) -> pd.DataFrame:
    """
    Example dataset mimicking a 2-arm randomized controlled trial with responders and non-responders

    Contains the following variables:

     * `treatment`: 1:1 drugA vs. drugB
     * `response`: drugA: 1:3 responder vs. non_responder, drugB: 3:1 resonder vs. non_responder
     * `biomarker`: a continuous variable with values drawn from the following normal distributions:

    Parameters
    ----------
    size
        dataset size, must be a multiple of 8
    seed
        random seed
    """
    random.seed(seed)
    rngs = {
        ("drugA", "responder"): (5, 2),
        ("drugA", "non_responder"): (7, 2.2),
        ("drugB", "responder"): (10, 4),
        ("drugB", "non_responder"): (5, 3),
    }

    if size % 8:
        raise ValueError("Dataset size must be a multiple of 8")

    S = int(size / 8)

    return (
        pd.DataFrame()
        .assign(
            treatment=["drugA"] * 4 * S + ["drugB"] * 4 * S,
            response=["non_responder"] * S + ["responder"] * 3 * S + ["non_responder"] * 3 * S + ["responder"] * S,
        )
        .assign(
            biomarker=lambda x: [
                random.normalvariate(*rngs[(treatment, response)])
                for treatment, response in zip(x["treatment"], x["response"], strict=False)
            ]
        )
    )
