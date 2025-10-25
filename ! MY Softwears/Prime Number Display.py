# Prime Number Display
fast = int(input('Fast: - '))
last = int(input('Last: - '))

for num in range (fast , last +1):
    if num >1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num,end=(' , '))


