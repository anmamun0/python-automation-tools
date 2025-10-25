# ls  = (i  for i in range(10))
# print(ls.__next__())
# print(ls.__next__())
# print(ls.__next__())

# print('hell')

# ls = [i for i in range(10)]
# print(ls)

dic = {i:f'item {i}'  for i in range(10)}

dic2 = {i:f'item {i}'  for i in range(10)}
dic3 = {value : key for key, value in dic2.items()}

print(dic)
print(dic3)

dresses = {dress for dress in ['dress1', 'dress2','dress2','dress1','dress1']}
print(dresses)

para = (i for i in range(2,100000) if i%100 == 0)
print(para.__next__())
print(para.__next__())
