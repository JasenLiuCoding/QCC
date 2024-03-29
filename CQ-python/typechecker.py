# functions for typechecker including:
import lark
from helpers import *
#  type_program(p)
#  type_procedure_parameters(p,type_env)
#  type_parameter_declaration(d,type_env)
#  type_lval(l,type_env)
#  type_procedure(p,type_env)
#  type_statement(s,type_env)
#  type_exp(e,type_env)
#  type_declaration(d,type_env)
#  type_gate(g,type_env)
#  type_qupdate(q,type_env)


def type_exp(e:lark.tree.Tree, type_env:dict):
    # check if e is a value
    match(node_name(e)):
        case 'INT': return 'int'
        case 'FLOAT': return 'float'
    # if e is not a value means there are subexpressions
    rule = node_rule(e, "expression")
    try:
        match(rule):
            case [_, "BINOP",_] | [_, 'PE', _] | [_, 'MD', _] | [_, 'AS', _]:
                # binary operator
                e1, _, e2 = e.children  # get two side of expression
                t1, t2 = type_exp(e1, type_env), type_exp(e2, type_env) # type check two side of expression
                tm = max_type(t1, t2)   # find the max type of this two side
                if (tm is None):
                    raise TypeError(f"Incompatible types: {t1} and {t2} in {rule}")
                return tm
            case ['expression__UNOP', _]:
                # unary operation
                _, e1 = e.children # get expression
                print(e1)
                t = type_exp(e1, type_env)
                if t is None:
                    raise TypeError(f"Incompatible types: {t} in {rule}")
                return t
    except:
        raise Exception(f"Error evaluating rule: {rule} for node: {e}")
    
# def type_declaration(d:lark.tree.Tree , type_env: dict):

    
    
    


