class Programmer():
    company = 'Microsoft'

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getinfo(self):
        print(f'name of {self.company} programmer is {self.name}\nsalary of programmer{self.salary}')

anjali = Programmer("anjali",70000)
anjali.getinfo()
       


