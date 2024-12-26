print(2 - 3)
print(2 * 3)
print(2 + 3)
print(9 / 3)

def calculate(operator, number1, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        return "Sorry, IDK"

if __name__ == '__main__':
    print(__name__)



    