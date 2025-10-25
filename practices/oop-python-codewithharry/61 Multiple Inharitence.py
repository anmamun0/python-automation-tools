class Employee: 
    no_of_leavs = 8
    var = 1
    
    # constraction function
    def __init__(self, a, b,c ):
        self.name = a
        self.salary = b
        self.role = c
    def printdetails(self):
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


class Player():
    var = 2
    def __init__(self, name, game):
        self.name = name 
        self.game = game
        
    def printdetails(self):
        return f'name is {self.name}, salary is {self.game}'

class CoolProgrammer(Employee, Player):
    var = 3
    language = 'C++'
    def printlanguage(self):
        print(self.language)

mamun = Employee('AN.Mamun', 5000 , 'Program')
rohan = Employee('Rohan', 597, 'busnesser')



karan = CoolProgrammer('Karan', 777, 'coolProgrammer')
det = karan.printdetails()
print(det)
karan.printlanguage()