import pickle
cars = ['hello','mamun','BMW','Audi']

file = 'mycar.pkl'
# fileobj = open(file,'wb')

# pickle.dump(cars,fileobj)
# fileobj.close()

fileobj = open(file,'rb')
mycar= pickle.load(fileobj)
print(mycar)