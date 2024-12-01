from importlib.metadata import version

from . import datasets
from ._contrasts import FormulaicContrasts
from ._factor_metadata import FactorMetadata, get_factor_storage_and_materializer

__all__ = ["FormulaicContrasts", "FactorMetadata", "get_factor_storage_and_materializer"]
__version__ = version("formulaic-contrasts")
