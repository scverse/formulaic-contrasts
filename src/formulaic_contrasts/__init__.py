from importlib.metadata import version

from ._factor_metadata import AmbiguousAttributeError, FactorMetadata
from .contrast_builder import FormulaicContrasts

__all__ = ["FormulaicContrasts"]
__version__ = version("formulaic-contrasts")
