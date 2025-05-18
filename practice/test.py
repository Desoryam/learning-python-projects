class person:
    def __init__(self,name,clas,roll):
        self.name=name
        self.clas=clas
        self.roll=roll
    def show(self):
        return (f"my name is {(self.name).capitalize()} I study in {self.clas}th and my roll no. is 0{self.roll}")
    
    @staticmethod
    def pop(i,j):
        return f"{i*j}"

a=person("anas",12,7)
print(a.pop(98,119))
print(a.show())
