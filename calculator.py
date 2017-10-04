"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def is_valid_arguments(a_list):
    try:
        all(isinstance(float(token), int) for token in a_list)
        return True
    except ValueError:
        return False

def is_valid_operator(operator):
    if operator not in ["q", "square", "cube", "pow", "+", "-", "/", "*", "mod"]:
        return False
    else:
        return True





while True:
    print ">",
    input_string = raw_input().rsplit()
    tokens = input_string
    operator = tokens[0]


    if not is_valid_operator(tokens[0]):
        print "Choose a valid operator or q(uit)"
        continue
    if not is_valid_arguments(tokens[1:]):
        print "Please only use valid arguments"
        continue
    if operator == "q":
        break

    elif len(tokens) == 1:
        print "Please check your operators arguments"
    elif len(tokens) == 2:
        num1 = tokens[1]
        if operator == "square":
            print square(float(num1))
        elif operator == "cube":
            print cube(float(num1))
        else:
            print "Please check your operators arguments"
    elif len(tokens) >= 3:
        if operator == "pow":
            print power_more(tokens[1:])
        elif operator == "+":
            print add_more(tokens[1:])
        elif operator == "-":
            print subtract_more(tokens[1:])
        elif operator == "*":
            print multiply_more(tokens[1:])
        elif operator == "mod":
            print mod_more(tokens[1:])
        elif operator == "/":
            print divide_more(tokens[1:])
        else:
            print "Please check your operators arguments"
