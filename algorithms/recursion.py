def factorial_iterative(number):
    product = None
    for factor in range(1, number +1):
        if factor == 1:
            product = factor
        else:
            product *= factor
    return product


def factorial_recursive(number):
    product = number
    if number == 1:
        return product
    else:
        return factorial_recursive(number-1) * product