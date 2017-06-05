#13. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print tp1
print tp2

''' output
[root@test python]# python program13.py
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)
'''
