# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Functions.ColorTupleConversion import (
    hex_to_rgb,
    rgb_to_hex
)
from .RGB import RGB
from ._Bases import _HEX

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# inherits from rgb as it is just another notation of the rgb format
class HEX(RGB,_HEX):
    """
    Color Object for HEX values.
    Inherits from RGB as this is just another notation for RGB values.
    """
    def __init__(self, hex_value:str):
        if not isinstance(hex_value,str):
            raise ValueError(f"HEX value {hex_value=} did not consist of a string value")
        super().__init__(*hex_to_rgb(hex_value))

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return rgb_to_hex(self.r,self.g,self.b)

    def __repr__(self) -> str:
        return f"HEX(r={self.r},g={self.g},b={self.b})"