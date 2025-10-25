n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()


print('2nd way ')
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(j+1,end=" ")
    print()


print('3rd')
# Function to print pyramid shape
def pyramid(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "* "*i)

# Example usage
pyramid(5)



print('4th')
# Function to print pyramid shape
def pyramid(n):
    for i in range(n, 0, -1):
        print(" "*(n-i) + "* "*i)

# Example usage
pyramid(5)
