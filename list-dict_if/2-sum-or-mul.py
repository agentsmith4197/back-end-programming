num1 = int(input("Enter the first integer "))
num2 = int(input("Enter the second integer "))

ans = num1 * num2

if ans <= 1000:
	print(f'the produt of {num1} and {num2} = {ans}')
	
else:
	ans = num1 + num2
	print(f'the sum of {num1} and {num2} = {ans}')