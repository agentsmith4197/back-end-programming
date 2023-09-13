def hexacode(userInput):
    hexa = ''.join(format(ord(char), '02x') for char in userInput)
    
    return hexa
user_input = input("write some stuff$  ")

result = hexacode(user_input)
print( result)
