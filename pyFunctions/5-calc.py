def calc(num1, num2, operator):
    result = None
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero!"
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Cannot calculate modulus with zero!"
    else:
        return "Invalid operator"
    
    return result

while True:
    input_str = input("Enter an expression (e.g., 1 + 2) or 'exit' to quit: ")
    
    if input_str.lower() == 'exit':
        print("thank you come back again$ ")
        break
    
    try:
        num1, operator, num2 = input_str.split()
        num1 = float(num1)
        num2 = float(num2)
        
        result = calc(num1, num2, operator)
        if operator == "+":
            print(f'The sum of {num1} + {num2} = {result}')
        elif operator == "-":
        	print(f'The difference of {num1} - {num2} = {result}')
        elif operator == "/":
        	print(f'The division of {num1} / {num2} = {result}')
        elif operator == "*":
        	print(f'The difference of {num1} * {num2} = {result}')
        elif operator == "%":
        	print(f'The remaindant of {num1} and {num2} = {result}')
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input. Use the format 'number operator number'.")
