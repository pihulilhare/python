raw_#10.Define a function that computes the length of a given list or string.

def countStringLength(inputString):
#DocString
# Function to calculate the string length
	count = 0
	for i in inputString:
		count = count+1
	print ("Length of the String is " +str(count))
print ("Enter string")
inputString = raw_input()
countStringLength(inputString)

'''Output
[root@test python]# python program10.py
Enter string
Priyanka Lilhare
Length of the String is 16
'''
