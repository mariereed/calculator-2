"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2

def add_more(your_list):
    sum = 0
    for number in your_list:
        sum += float(number)
    return sum


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2

def subtract_more(your_list):
    result = float(your_list[0])
    for number in your_list[1:]:
        result -= float(number)
    return result

def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2

def multiply_more(your_list):
    result = float(your_list[0])
    for number in your_list[1:]:
        result *= float(number)
    return result 


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return float(num1) / num2

def divide_more(your_list):
    result = float(your_list[0])
    for number in your_list[1:]:
        result /= float(number)
    return result 


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1

def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator

def power_more(your_list):
    result = float(your_list[0])
    for number in your_list[1:]:
        result = result ** float(number)
    return result

def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2

def mod_more(your_list):
    result = float(your_list[0])
    for number in your_list[1:]:
        result = result % float(number)
    return result