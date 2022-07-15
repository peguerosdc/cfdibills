"""
Helper fields to be used by CFDIs.
"""

from decimal import Decimal

from pydantic import condecimal, constr

RFC = constr(
    regex=r"[A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]", strip_whitespace=True
)

CURP = constr(regex=r"[A-Z&Ñ]{4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]")

NonNegativeSixDecimals = condecimal(ge=Decimal(0), decimal_places=6)

PositiveSixDecimals = condecimal(ge=Decimal(0.000001), decimal_places=6)
