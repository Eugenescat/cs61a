import re


def calculator_ops(calc_str):
    """
    Finds expressions from the Calculator language that have two
    numeric operands and returns the expression without the parentheses.

    >>> calculator_ops("(* 2 4)")
    ['* 2 4']
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    ['* 2 4', '+ 3 5', '- 10 7']
    >>> calculator_ops("(* 2)")
    []
    """
    # ([-+*/]): The hyphen - is placed at the beginning of the character class to avoid being interpreted as a range operator. 
    # \( and \) match the literal parentheses.
    # ([-+*/] \d+ \d+) is a capturing group for the operator followed by two numbers, each separated by spaces. This group captures the entire expression inside the parentheses without including the parentheses themselves.
    return re.findall(r'\(([-+*/]\s\d+\s\d+)\)', calc_str)
