from inspect import cleandoc


class IntOperation:
    """
    A node that performs an arithmetic operation on two integers.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        """
        return {
            "required": {
                "operand_a": ("INT", {"display": "number"}),
                "operand_b": ("INT", {"display": "number"}),
                "operator": (["+", "-", "*", "/"],),
            },
        }

    DESCRIPTION = cleandoc(__doc__)
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "process"
    CATEGORY = "Mewins Node Pack"

    def process(self, operand_a, operand_b, operator) -> (int,):
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
                return (int(operand_a / operand_b),)
