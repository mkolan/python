# uestion:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class Myexample:
    def __init__(self):
        self.s =  ""

    def getString(self):
        self.s = input("Enter your input: ")

    def printString(self):
        return self.s



obj = Myexample()
obj.getString()
print(obj.printString())