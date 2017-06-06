#10.Define a function that computes the length of a given list or string.

def countStringLength(inputString):
	
 #DocString
 # Function to calculate the string length
	count = 0
for i in inputString:
	count = count+1
print ("Length of the String is " +str(count))
print ("Function to find the length of the input String")
print ("Enter string")
inputString = input()
countStringLength(inputString)
