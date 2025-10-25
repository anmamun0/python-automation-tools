
print('''Here's some sample Python code that will generate the Fibonacci sequence up to a certain number of terms:''')
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            next_term = fib_list[i-1] + fib_list[i-2]
            fib_list.append(next_term)
        return fib_list
print(fibonacci(5))



print('Different-Way')
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
print(fibonacci(10))


import Factorial_Number 
Factorial_Number.factorial_Number()