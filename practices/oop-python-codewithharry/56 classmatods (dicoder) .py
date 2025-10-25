class Employee: 
    no_of_leavs = 8
    
    # constraction function
    def __init__(self, a, b,c ):
        self.name = a
        self.salary = b
        self.role = c

    
    def fast(self):
        return f'name is {self.name}, salary is {self.salary}, and role is {self.role}'
    
    # dacorator
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leavs = newleaves

    
mamun = Employee('AN.Mamun', 5000 , 'Program')

print(mamun.fast())

mamun.change_leaves(99)
print(mamun.no_of_leavs)