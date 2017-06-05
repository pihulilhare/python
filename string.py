Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def countStringLength(inputString):
 #DocString
 """ Function to calculate the string length"""
 
count = 0
 
for i in inputString:
 count = count+1
 
print ("Length of the String is " +str(count))
 
print ("Function to find the length of the input String")
print ("Enter string")
 
inputString = input()
 
countStringLength(inputString)
