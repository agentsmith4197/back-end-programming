myList = [2, 1, 'This', 4, '10', (3, 2), 'fun']

myList_integer = []

for item in myList:
    if isinstance(item, int):
        myList_integer.append(item)
#sorted_integer_list = sorted(myList_integer)

print(myList_integer)
