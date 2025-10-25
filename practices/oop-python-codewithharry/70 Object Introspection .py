class Employee:
    def __init__(self, fname , lname) :
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@ancoder.com"
    def explain(self):
        return f'This employee is {self.fname} {self.lname}'
    '''he is '''
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return ' Email is not set.! Please set it using setter'
        return f"{self.fname}.{self.lname}@ancoder.com"
    
    @email.setter
    def email(self, string):
        print('Setting Now...')
        # names = string.split('@')[0]
        # self.fname = names.split('.')[0]
        # self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None



skillf = Employee('skill', 'F')
# print(skillf.email)
# o= 'this is a astring'
# print(id('this is a astritg'))
# print(dir(o))

import inspect
ab = inspect.getmembers(skillf)

for i in ab:
    print(i)