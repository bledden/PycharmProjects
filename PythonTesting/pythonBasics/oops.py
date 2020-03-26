# Hi! This was made by Blake

class Calculator:
    num = 100

    def getData(self):
        print("I am now executing  a method in a class")


obj = Calculator() # Sets the class to a variable
obj.getData() # Calls the method in the class (which prints the string)
obj.num # This calls the class but does nothing with the value
print(obj.num) # Prints the value called from the class with the variable obj

