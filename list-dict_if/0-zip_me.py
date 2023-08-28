lst1 = ["ten", "twenty", "thirty"]
lst2 = ["10", "20", "30"]

output_dict = dict(zip(lst1, map(int, lst2)))
print(output_dict)