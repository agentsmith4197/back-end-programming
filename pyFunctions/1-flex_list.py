myList = [2, 1, "this", 4, "10", (3, 2), "fun", "python"]
first = "Number"
second = "Alphabet"
third = "strings"

def new_list(values):
    if values == first.lower():
        return [item for item in myList if isinstance(item, int)]
    elif values == third.lower():
        return [item for item in myList if isinstance(item, str)]
    elif values == second.lower():
        return [item for item in myList if isinstance(item, str) and item.isalpha()]
    else:
        return "Invalid option"

number = input("Enter 'Numbers' ")
string = input("Enter 'Strings' ")
alphabet = input("Enter 'Alphabet': ")

Number = new_list(number)
print(Number)

String = new_list(string)
print(String)

Alphabet = new_list(alphabet)
print(Alphabet)
