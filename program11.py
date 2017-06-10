'''11.Write a program that accepts a sentence and calculate the number of letters and digits.
              Suppose the following input is supplied to the program:
              i/p: Hello Priya 1287
              o/p: LETTERS 10
                     DIGITS 4'''

s = raw_input("Enter the Sentence")
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]


'''Output
[root@test python]# python program11.py
Enter the Sentence This Is The Python String
LETTERS 21
DIGITS 0'''
