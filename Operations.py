def multiply(a ,b):
    return a * b

def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"

def add(a, b):
    return a + b

def exponent(a, b):
    return a ** b

def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Can't subtract strings"

print("Adding lines for another commit")
print("Adding more lines for another commit")