from mewins_node_pack.int_operation import IntOperation
from mewins_node_pack.simple_expression import SimpleExpression
from mewins_node_pack.float_operation import FloatOperation
from mewins_node_pack.float_to_int import FloatToInt
from mewins_node_pack.int_to_float import IntToFloat


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "SimpleExpression": SimpleExpression,
    "IntOperation": IntOperation,
    "FloatOperation": FloatOperation,
    "FloatToInt": FloatToInt,
    "IntToFloat": IntToFloat,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleExpression": "Simple Expression",
    "IntOperation": "Int Operation",
    "FloatOperation": "Float Operation",
    "FloatToInt": "Float to Int",
    "IntToFloat": "Int to Float",
}
