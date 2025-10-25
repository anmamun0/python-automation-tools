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
    @classmethod
    def from_str(cls,string):
        # params = string.split('-')
        # print(params)
        # return cls(params[0], params[1], params[2])
        
        return cls(*string.split('-'))
    

    
mamun = Employee('AN.Mamun', 5000 , 'Program')
second = Employee.from_str('Karan-9989-studen')

print(second.salary)
print(second.no_of_leavs)



