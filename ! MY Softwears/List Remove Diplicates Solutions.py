# List Remove Duplicates Solutions
my_list = [1, 2, 3, 4, 2, 1, 5]
my_list = list(set(my_list))
print(my_list) # [1, 2, 3, 4, 5]

# Different-Way List Remove Duplicates Solutions
my_list = [1, 2, 3, 4, 2, 1, 5]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
my_list = new_list
print(my_list) # [1, 2, 3, 4, 5]
print("AN.Mamun")
