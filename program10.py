#10.Define a function that computes the length of a given list or string.

print ("")
print ("Function to find the length of the List")
 
List = [2,1,8,6,5,9,3]
 
print ("The list is " +str(List))
def countListLength(List):
	listCount = 0
 
for i in List:
	listCount = listCount+1
	return listCount
 
print("Length of the list is " +str(countListLength(List)))