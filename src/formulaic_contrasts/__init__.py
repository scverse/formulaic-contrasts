from importlib.metadata import version

from ._contrasts import FormulaicContrasts
from ._factor_metadata import AmbiguousAttributeError, FactorMetadata

__all__ = ["FormulaicContrasts"]
__version__ = version("formulaic-contrasts")
