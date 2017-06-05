'''11.Write a program that accepts a sentence and calculate the number of letters and digits.
              Suppose the following input is supplied to the program:
              i/p: Hello Priya 1287
              o/p: LETTERS 10
                     DIGITS 4'''




s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)