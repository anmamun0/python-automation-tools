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
    @staticmethod
    def printgood(string):
        return 'This is good  ' + string
    
# clild class of Employee
class programmer(Employee): 
    def printprog(self):
        return f'The child programmer is {self.name}, Salary is {self.salary}, and role is{self.role}'
    

# clild class of Employee
class programmer2(Employee):
    def __init__(self, a, b, c, lang):
        self.name = a
        self.salary = b
        self.role = c
        self.language = lang

        
    def printprog(self):
        return f'The child programmer is {self.name}, Salary is {self.salary}, and role is{self.role}, know language {self.language}'

    
mamun = Employee('AN.Mamun', 5000 , 'Program')
rohan = Employee('Rohan', 597, 'busnesser')

subham = programmer("Shubam", 444, 'Programmer')
karan = programmer('Karan', 666, ' programmer')

karan2 = programmer2('Karan', 666, ' programmer', ['python'])


print(karan2.printprog())

