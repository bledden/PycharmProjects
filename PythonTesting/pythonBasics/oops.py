# Hi! This was made by Blake


class Calculator:
    num = 100  # class variables
    ques = []

    # Default constructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("I am called automatically when the object is created with Calculator()")  # The objects are obj & obj1

    def getData(self):
        print("I am now executing  a method in a class")

    def summation(self):
        c = self.firstNum + self.secondNum + self.num
        return c
        # print(c)  # Must perform print inside of the function

    def diff(self):
        return self.firstNum - self.secondNum
        # print(m)


obj = Calculator(500, 80)  # Sets the class to a variable
obj.getData()  # Calls the method in the class (which prints the string)
# obj.num <-- This calls the class but does nothing with the value
print(obj.num)  # Prints the value called from the class with the variable obj
print(obj.summation())
print(obj.diff())  # Prints the value returned by obj.diff

obj1 = Calculator(60, 9)
obj1.summation()
print(obj1.diff())



