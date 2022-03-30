# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Functions.BoilerPlate import (
    Constrain,
    TestTypes
)
from ._ColorSystem import (
    ColorSystem,
    _HSV
)

# ------------------------------------------------------------------------------------------------------------------
# - Color -
# ------------------------------------------------------------------------------------------------------------------
class HSV(ColorSystem,_HSV):
    # ------------------------------------------------------------------------------------------------------------------
    # INIT method
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,h: int|float, s: int|float, v: int|float):
        if not TestTypes(types=(int,float),objects=(h,s,v)):
            raise ValueError(f"HSV values {h=},{s=},{v=} did not consist of integer or float values")

        self.h = h
        self.s = s
        self.v = v

    # ------------------------------------------------------------------------------------------------------------------
    # RGB Properties
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def h(self):
        return self._h
    @h.setter
    def h(self, value: int | float):
        self._h = Constrain(value, 360)

    @property
    def s(self):
        return self._s
    @s.setter
    def s(self, value: int | float):
        self._s = Constrain(value, 1)

    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, value: int | float):
        self._v = Constrain(value, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # MAGIC Methods
    # ------------------------------------------------------------------------------------------------------------------
    # String magic methods
    def __str__(self) -> str:
        return f"{self.h};{self.s};{self.v}"

    def __repr__(self) -> str:
        return f"HSV(h={self.h}, s={self.s}, v={self.v})"