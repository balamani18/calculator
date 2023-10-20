class Calculator:
    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            return "Division by zero is not allowed."
        return a / b

if __name__ == "_main_":
    calc = Calculator()

    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'exit' to end the program")
        user_input = input(": ")

        if user_input == "exit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result:", calc.add(num1, num2))
            elif user_input == "subtract":
                print("Result:", calc.subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", calc.multiply(num1, num2))
            elif user_input == "divide":
                print("Result:", calc.divide(num1, num2))
        else:
            print("Invalid input")