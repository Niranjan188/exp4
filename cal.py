import sys
print("--- Standard Calculator ---")
while True:
    try:
        user_input = input("Enter calculation (e.g., 10 + 5) or 'exit': ")
        if user_input.lower() == 'exit': sys.exit()
        
        parts = user_input.split()
        if len(parts) != 3:
            print("Error: Use format 'Value Operator Value'")
            continue
            
        num1, op, num2 = float(parts[0]), parts[1], float(parts[2])
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': 
            result = num1 / num2 if num2 != 0 else "Undefined (Div by 0)"
        else: result = "Invalid Operator"
        
        print(f"Result: {result}\n")
    except ValueError:
        print("Invalid input! Please enter numbers correctly.")
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Div by 0"

operations = {"+": add, "-": sub, "*": mul, "/": div}

def run_calculator():
    print("Functions-based Calc (Type 'q' to quit)")
    while True:
        op_choice = input("Select (+, -, *, /): ")
        if op_choice.lower() == 'q': break
        if op_choice not in operations:
            print("Invalid choice!")
            continue
        try:
            v1 = float(input("First number: "))
            v2 = float(input("Second number: "))
            calc_func = operations[op_choice]
            print(f"Output: {calc_func(v1, v2)}\n")
        except ValueError:
            print("Numeric input required.")

run_calculator()
class PowerCalc:
    def __init__(self):
        self.current = 0.0

    def process(self, op, val):
        try:
            if op == '+': self.current += val
            elif op == '-': self.current -= val
            elif op == '*': self.current *= val
            elif op == '/': self.current /= val
            elif op == 'c': self.current = 0.0
            return self.current
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"

calc = PowerCalc()
print("OOP Calculator: Commands: +, -, *, /, c (clear), s (stop)")
while True:
    cmd = input(f"({calc.current}) Operation & Value: ").split()
    if cmd[0] == 's': break
    if len(cmd) < 2 and cmd[0] != 'c': continue
    
    op = cmd[0]
    val = float(cmd[1]) if len(cmd) > 1 else 0
    print(f"Total: {calc.process(op, val)}")