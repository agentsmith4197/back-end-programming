dict1 = {"ten": 10, "twenty": 20, "thirty":30}
dict2 = {"thirty": 30, "fourty": 40, "fifty":50}

merged_dict = {**dict1, **dict2}
print(merged_dict)