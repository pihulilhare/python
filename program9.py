#9. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.  

function maxOfThree(a, b, c):
	if ((a >= b) && (a >= c)) :  
		return a;
	else if ((b >= a) && (b >= c)):
		return b;
	else:	
		return c;
    
print(maxOfThree(343,35124,42))