class Employee:
    def __init__(self, fname , lname) :
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@ancoder.com"
    def explain(self):
        return f'This employee is {self.fname} {self.lname}'
    
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



Bangladesh = Employee('Bangledesh','supporter')
# mamun = Employee('AN', 'Mamun')

print(Bangladesh.explain())
print(Bangladesh.email)

Bangladesh.fname = 'US'
print(Bangladesh.email)

Bangladesh.email = 'this.that@codewithharry.com'  #setter  decorators
print(Bangladesh.email)

# del Bangladesh.email                            #deleter decorator
# print(Bangladesh.email)