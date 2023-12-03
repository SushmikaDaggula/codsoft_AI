class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")

class CalculationHistory:
    def __init__(self):
        self.history = []

    def add_to_history(self, num1, num2, operation, result):
        entry = {'num1': num1, 'num2': num2, 'operation': operation, 'result': result}
        self.history.append(entry)

    def display_history(self):
        print("Calculation History:")
        for entry in self.history:
            print(f"{entry['num1']} {entry['operation']} {entry['num2']} = {entry['result']}")

def get_user_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    return num1, num2, operation

def main():
    calculator = Calculator()
    history = CalculationHistory()

    while True:
        try:
            num1, num2, operation = get_user_input()

            if operation in calculator.operations:
                result = calculator.operations[operation](num1, num2)
                print(f"Result: {result}")

                history.add_to_history(num1, num2, operation, result)
            else:
                print("Invalid operation. Please enter +, -, *, or /.")

        except ValueError as e:
            print(f"Error: {e}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            history.display_history()
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
