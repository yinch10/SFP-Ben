def calculate(num1, operater, num2):
    if operater == "+":
        return num1 + num2
    elif operater == "-":
        return num1 - num2
    elif operater == "*":
        return num1 * num2
    elif operater == "/":
        return num1 / num2
    else:
        return "Invalid operator"
    
print(calculate(10, "+", 10))
print(calculate(10, "-", 10))
print(calculate(10, "*", 10))
print(calculate(10, "/", 10))