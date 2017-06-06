
#1. Write a python script for creating directory,displaying its contents. 
# Create a file named Directory1.py
#vi Directory1.py
#In this file wirte code
import os,sys
os.mkdir("Priyanka")
os.chdir("Priyanka")
os.system("touch file1")
os.system ("ls") # it will list all the files and directories
os.system("cat file1") 

'''OUTPUT
program1.py
file1'''
