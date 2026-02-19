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