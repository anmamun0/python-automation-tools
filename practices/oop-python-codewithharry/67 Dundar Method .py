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
    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return f"Employes ('{self.name}' {self.salary}, '{self.role}')"
    def __str__(self):
        return "this is str "

emp = Employee('Mamun', 500, 'programmer')
emp2 = Employee('Rohan', 50, 'Student')

print(emp / emp2 )
print(emp)
print(emp2)
