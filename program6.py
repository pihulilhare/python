#6. Write a program that takes inputs from user their name and their age. And display the year in which they will turn 100 years old.

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)