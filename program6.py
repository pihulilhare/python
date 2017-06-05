#6. Write a program that takes inputs from user their name and their age. And display the year in which they will turn 100 years old.

name = raw_input("What is your name: ")
age = int(raw_input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)

'''output
What is your name: Priyanka Lilhare
How old are you: 23
Priyanka Lilhare will be 100 years old in the year 2091'''
