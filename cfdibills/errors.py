"""
Custom errors definition.
"""


class UnsupportedCFDIError(Exception):
    """Raised when a XML contains a CFDI of an unsupported version"""

    pass


class InvalidCFDIError(Exception):
    """Raised when a CFDI in an XML could not be parsed"""

    pass


class ComplementoNotFoundError(Exception):
    """Raised when a CFDI doesn't have a Complemento of a specific type."""

    pass
