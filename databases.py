import sqlite3
conn = sqlite3.connect('employee.db')
c = conn.cursor()
# Create table

'''cur.execute("DROP TABLE IF EXISTS Cars")
   cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
   cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)'''
c.execute("DROP TABLE IF EXISTS Employee")
c.execute('''CREATE TABLE Employee (Emp_Id, Emp_Name, Salary, MobileNo)''')

print "Table Creation done successfully";
# Insert a row of data
c.execute("INSERT INTO Employee VALUES ('1','Priya Lilhare','30000',9907736969)")
print "Insertion done successfully";
#Display Data
c.execute("SELECT Emp_Id, Emp_Name, Salary, MobileNo from Employee")
for row in c:
   print "Emp_Id = ", row[0]
   print "Emp_Name = ", row[1]
   print "Salary = ", row[2]
   print "MobileNo = ", row[3], "\n"
print "Display done successfully";

#Update Data
c.execute("UPDATE Employee  set Salary = 50000 where Emp_Id = 1")
c.commit() 
print "Updation done successfully";
print "Total number of rows updated :", conn.total_changes
#Display Data
c.execute("SELECT Emp_Id, Emp_Name, Salary, MobileNo from Employee")
for row in c:
   print "Emp_Id = ", row[0]
   print "Emp_Name = ", row[1]
   print "Salary = ", row[2]   
   print "MobileNo = ", row[3], "\n"
print "Display updated Data";

# Insert a row of data
c.execute("INSERT INTO Employee VALUES ('2','Yatika Verma','40000',8989166152)")
print "Insertion done successfully";
#Display Data
c.execute("SELECT Emp_Id, Emp_Name, Salary, MobileNo from Employee")
for row in c:
   print "Emp_Id = ", row[0]
   print "Emp_Name = ", row[1]
   print "Salary = ", row[2]
   print "MobileNo = ", row[3], "\n"
print "Display updated Data";

#Delete data
c.execute("DELETE from Employee where Emp_Id = 2;")
c.commit() 
print "Total number of rows deleted :", conn.total_changes
c.execute("SELECT Emp_Id, Emp_Name, Salary, MobileNo from Employee")
for row in c:
   print "Emp_Id = ", row[0]
   print "Emp_Name = ", row[1]
   print "Salary = ", row[2]
   print "MobileNo = ", row[3], "\n"
print "Deletion done successfully";

#Display Data

c.execute("SELECT Emp_Id, Emp_Name, Salary, MobileNo from Employee")
for row in c:
   print "Emp_Id = ", row[0]
   print "Emp_Name = ", row[1]
   print "Salary = ", row[2]
print "Display updated Data";
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
'''OUTPUT
Table Creation done successfully
Insertion done successfully

Emp_Id =  1
Emp_Name =  Priya Lilhare
Salary =  30000
MobileNo =  9907736969 

Display done successfully
Updation done successfully
Total number of rows updated : 1

Emp_Id =  1
Emp_Name =  Priya Lilhare
Salary =  30000
MobileNo =  9907736969 

Display updated Data

Insertion done successfully

Emp_Id =  1
Emp_Name =  Priya Lilhare
Salary =  30000
MobileNo =  9907736969 

Emp_Id =  2
Emp_Name =  Yatika Verma
Salary =  40000
MobileNo =  8989166152

Display updated Data
Total number of rows deleted : 2
Emp_Id =  1
Emp_Name =  Priya Lilhare
Salary =  30000
MobileNo =  9907736969 

Emp_Id =  2
Emp_Name =  Yatika Verma
Salary =  40000
MobileNo =  8989166152 

Deletion done successfully

Emp_Id =  1
Emp_Name =  Priya Lilhare
Salary =  30000

Emp_Id =  2
Emp_Name =  Yatika Verma
Salary =  40000

Display updated Data

[root@test python]# '''

