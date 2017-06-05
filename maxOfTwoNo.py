# 8 Define a function max() that takes two numbers as arguments and returns the largest of them.

def max (firstNo, secondNo):
	if firstNo > secondNo:
		return firstNo8
	else:
		return secondNo

def getNumbersFromUser():
	userFirstNo = int(input("enter First Number:"))
	userSecondNo = int(input("enter Second Number:"))
	return userFirstNo, userSecondNo

def main():
	userFirstNo, userSecondNo = getNumbersFromUser()
	print ("The Maximum Numbers Between", userFirstNo,"and" , userSecondNo, "is" , max(userFirstNo, userSecondNo))
main()