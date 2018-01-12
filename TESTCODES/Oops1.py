
class Employee:

    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class developement(Employee):
    pass

emp1=developement('jala','Maharana',2000)
emp2=Employee('Tarani','Sahoo',3000)

help(emp1)
