from inspect import cleandoc


class FloatOperation:
    """
    A node that performs an arithmetic operation on two floats.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        """
        return {
            "required": {
                "operand_a": ("FLOAT", {"display": "number"}),
                "operand_b": ("FLOAT", {"display": "number"}),
                "operator": (["+", "-", "*", "/"],),
            },
        }

    DESCRIPTION = cleandoc(__doc__)
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "process"
    CATEGORY = "Mewins Node Pack"

    def process(self, operand_a, operand_b, operator) -> (float,):
        """
        Evaluate the expression and return the result.
        """
        match operator:
            case "+":
                return (operand_a + operand_b,)
            case "-":
                return (operand_a - operand_b,)
            case "*":
                return (operand_a * operand_b,)
            case "/":
                return (operand_a / operand_b,)
