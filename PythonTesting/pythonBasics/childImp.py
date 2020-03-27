# Hi! This was made by Blake Ledden

# This file is a child class of oops.py

from oops import Calculator  # This is how you import classes "from (file name) import (Class name)"


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 30, 50)
        print("An object has been created with this class - ChildImp")

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj3 = ChildImp()
print(obj3.getCompleteData())
