my_string = "python is a cool program"
for char in my_string:
    ascii_value = ord(char)
    binary_equivalent = format(ascii_value, '08b')
    print(binary_equivalent, end=' ')
