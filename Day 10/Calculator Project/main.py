import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(art.logo)

def calculator():
    should_continue = True
    n1 = float(input("Enter a number: "))
    while should_continue:
        for operation in operations:
            print(operation)
        choose_operation = input(f"Choose operation: ")
        n2 = float(input("Enter another number: "))
        calculation_function = operations[choose_operation]
        result = calculation_function(n1, n2)
        print(f"{n1} {choose_operation} {n2} result: {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            n1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
