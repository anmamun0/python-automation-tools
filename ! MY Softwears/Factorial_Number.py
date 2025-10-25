def factorial_Number():
    user_data = int(input('Enter a number to translate Factorial Number; '))
    count = 1
    for i in range(1, user_data + 1 ):
        count *= i
    print('Loading...')
    print(f'Your Factorial Number is {count}')
factorial_Number()

fib_list = [0, 1]
next_term = fib_list[2-1] + fib_list[2-2]
fib_list.append(next_term)
print(fib_list)