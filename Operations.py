def multiply(a ,b):
    return a * b

def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"
