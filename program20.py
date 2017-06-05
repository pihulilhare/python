#20. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
n=raw_input("Enter the String:")
def palindrome(n):
    index=0
    check=True
    while index<len(n):
        if n[index]==n[-1-index]:
            index+=1
            return True
        return False
if palindrome(n)==True:
    print "It is a Palindrome"
else:
    print "It is not a Palindrome"

    #output   
'''[root@test python]# python program20.py
Enter the String:madam
It is a Palindrome
[root@test python]# '''
