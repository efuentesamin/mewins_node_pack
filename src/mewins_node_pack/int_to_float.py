from inspect import cleandoc


class IntToFloat:
    """
    A node that converts an integer to a float.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        """
        return {
            "required": {
                "int_value": ("INT", {"display": "number"}),
            },
        }

    DESCRIPTION = cleandoc(__doc__)
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "process"
    CATEGORY = "Mewins Node Pack"

    def process(self, int_value) -> (float,):
        """
        Convert the integer to a float.
        """
        return (float(int_value),)
