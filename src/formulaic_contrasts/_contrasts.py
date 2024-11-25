import itertools

import pandas as pd

from ._factor_metadata import AmbiguousAttributeError, Factor, get_factor_storage_and_materializer, resolve_ambiguous


class FormulaicContrasts:
    def __init__(self, data: pd.DataFrame, design: str):
        """
        Initialize the contrast builder

        Parameters
        ----------
        data
            Metadata to be passed to formulaic
        design
            Formulaic formula of the model definition
        """
        self.factor_storage, self.variable_to_factors, materializer_class = get_factor_storage_and_materializer()
        self.design = materializer_class(data, record_factor_metadata=True).get_model_matrix(design)

    @property
    def variables(self):
        """Get the names of the variables used in the model definition."""
        try:
            return self.design.model_spec.variables_by_source["data"]
        except AttributeError:
            raise ValueError(
                "Retrieving variables is only possible if the model was initialized using a formula."
            ) from None

    def cond(self, **kwargs):
        """
        Get a contrast vector representing a specific condition.

        Parameters
        ----------
        **kwargs
            column/value pairs.

        Returns
        -------
            A contrast vector that aligns to the columns of the design matrix.
        """
        if self.factor_storage is None:
            raise RuntimeError(
                "Building contrasts with `cond` only works if you specified the model using a formulaic formula. Please manually provide a contrast vector."
            )
        cond_dict = kwargs
        if not set(cond_dict.keys()).issubset(self.variables):
            raise ValueError(
                "You specified a variable that is not part of the model. Available variables: "
                + ",".join(self.variables)
            )
        for var in self.variables:
            if var in cond_dict:
                self._check_category(var, cond_dict[var])
            else:
                cond_dict[var] = self._get_default_value(var)
        df = pd.DataFrame([kwargs])
        return self.design.model_spec.get_model_matrix(df).iloc[0]

    def contrast(self, column, baseline, group_to_compare):
        """
        Build a simple contrast for pairwise comparisons.

        Parameters
        ----------
        column
            column in adata.obs to test on.
        baseline
            baseline category (denominator).
        group_to_compare
            category to compare against baseline (nominator).

        Returns
        -------
            Numeric contrast vector.
        """
        return self.cond(**{column: group_to_compare}) - self.cond(**{column: baseline})

    def _get_default_value(self, var):
        factor_metadata = self._get_factor_metadata_for_variable(var)
        if resolve_ambiguous(factor_metadata, "kind") == Factor.Kind.CATEGORICAL:
            try:
                tmp_base = resolve_ambiguous(factor_metadata, "base")
            except AmbiguousAttributeError as e:
                raise ValueError(
                    f"Could not automatically resolve base category for variable {var}. Please specify it explicity in `model.cond`."
                ) from e
            return tmp_base if tmp_base is not None else "\0"
        else:
            return 0

    def _get_factor_metadata_for_variable(self, var):
        factors = self.variable_to_factors[var]
        return list(itertools.chain.from_iterable(self.factor_storage[f] for f in factors))

    def _check_category(self, var, value):
        factor_metadata = self._get_factor_metadata_for_variable(var)
        tmp_categories = resolve_ambiguous(factor_metadata, "categories")
        if resolve_ambiguous(factor_metadata, "kind") == Factor.Kind.CATEGORICAL and value not in tmp_categories:
            raise ValueError(
                f"You specified a non-existant category for {var}. Possible categories: {', '.join(tmp_categories)}"
            )
