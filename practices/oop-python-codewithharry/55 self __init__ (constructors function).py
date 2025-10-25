class Employee: 
    no_of_leavs = 8
    
    # constraction function
    def __init__(self, a, b,c ):
        self.name = a
        self.salary = b
        self.role = c

    
    def fast(self):
        return f'name is {self.name}, salary is {self.salary}, and role is {self.role}'
    
mamun = Employee('AN.Mamun', 5000 , 'Program')

# mamun.name = 'AN.Mamun'
# mamun.salary = '1M'
# mamun.role = 'Programmer'

print(mamun.fast())