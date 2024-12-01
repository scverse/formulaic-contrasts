from importlib.metadata import version

from ._contrasts import FormulaicContrasts
from ._factor_metadata import AmbiguousAttributeError, FactorMetadata, get_factor_storage_and_materializer

__all__ = ["FormulaicContrasts", "AmbiguousAttributeError", "FactorMetadata", "get_factor_storage_and_materializer"]
__version__ = version("formulaic-contrasts")
