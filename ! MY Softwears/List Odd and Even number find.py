# List Odd and Even number find.py

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [n for n in my_list if n % 2 != 0]
even_numbers = [n for n in my_list if n % 2 == 0]
print("Odd Numbers:", odd_numbers) # [1, 3, 5, 7, 9]
print("Even Numbers:", even_numbers) # [2, 4, 6, 8, 10]

# Different-Way List Odd and Even number find.py

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
even_numbers = []
for n in my_list:
    if n % 2 != 0:
        odd_numbers.append(n)
    else:
        even_numbers.append(n)
print("Odd Numbers:", odd_numbers) # [1, 3, 5, 7, 9]
print("Even Numbers:", even_numbers) # [2, 4, 6, 8, 10]
print('AN.Mamun ')
