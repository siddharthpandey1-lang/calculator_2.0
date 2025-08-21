class Calculator:
    def __init__(self):
        self.result = None

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is undefined.")
        self.result = x / y
        return self.result

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def main():
    calc = Calculator()
    operations = {
        '1': ('Addition', calc.add),
        '2': ('Subtraction', calc.subtract),
        '3': ('Multiplication', calc.multiply),
        '4': ('Division', calc.divide)
    }

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")