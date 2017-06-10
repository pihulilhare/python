#12.Define a class which has two methods: getString: to get a string from console input.

class IOString():
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = raw_input()

    def printString(self):
        print(self.str1.upper())

str1 = IOString()
str1.getString()
str1.printString()
