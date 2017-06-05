#8. Define a function max() that takes two numbers as arguments and returns the largest of them.
'''def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


if __name__ == "__main__":
    print max(2, 5)
    print max(5, 2)
    print max(5, 5)'''
def max (firstNo, secondNo):
	if firstNo > secondNo:
		return firstNo 
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
'''output
[root@test python]# python program8.py
enter First Number:50
enter Second Number:40
('The Maximum Numbers Between', 50, 'and', 40, 'is', 50)'''
