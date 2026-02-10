from inspect import cleandoc


class FloatToInt:
    """
    A node that converts a float to an integer.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        """
        return {
            "required": {
                "float_value": ("FLOAT", {"display": "number"}),
            },
        }

    DESCRIPTION = cleandoc(__doc__)
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "process"
    CATEGORY = "Mewins Node Pack"

    def process(self, float_value) -> (int,):
        """
        Convert the float to an integer.
        """
        return (int(float_value),)
