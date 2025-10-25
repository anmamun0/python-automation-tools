class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def idance(self):
        return f' Yes I dance {self.dance} no of times'

class Grandson(Son):
    pass
    # dance = 6 
    # def idance(self):
    #     return f' Jakson Jance I know {self.dance} no of times' 
    
darry = Dad()
larry = Son()
harry = Grandson()
print(harry.idance())