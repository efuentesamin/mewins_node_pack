from inspect import cleandoc


class SimpleExpression:
    """
    A logical expression that can be evaluated to a boolean value.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        """
        return {
            "required": {
                "operand_a": ("INT,FLOAT", {"display": "number"}),
                "operand_b": ("INT,FLOAT", {"display": "number"}),
                "operator": (["=", "!=", ">", "<", ">=", "<="],),
            },
        }

    DESCRIPTION = cleandoc(__doc__)
    RETURN_TYPES = ("BOOL",)
    RETURN_NAMES = ("result",)
    FUNCTION = "process"
    CATEGORY = "Mewins Node Pack"

    def process(self, operand_a, operand_b, operator) -> (bool,):
        """
        Evaluate the expression and return the result.
        """
        match operator:
            case "=":
                return (operand_a == operand_b,)
            case "!=":
                return (operand_a != operand_b,)
            case ">":
                return (operand_a > operand_b,)
            case "<":
                return (operand_a < operand_b,)
            case ">=":
                return (operand_a >= operand_b,)
            case "<=":
                return (operand_a <= operand_b,)
