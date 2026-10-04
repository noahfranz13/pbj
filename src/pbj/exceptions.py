"""
Custom exceptions for the PB&J package
"""

class InvalidIngredientError(Exception):
    """
    Exception thrown when the user requests something that is currently not supported
    by the API.
    """

    def __init__(self, invalid_ingredient):
        self.msg = f"{invalid_ingredient} does not belong on a PB&J sandwich!"

    def __str__(self):
        return self.msg

