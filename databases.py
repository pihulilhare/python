import sqlite3
conn = sqlite3.connect('employee.db')
c = conn.cursor()
# Create table
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
print "Display updated Data";
#Delete data
c.execute("DELETE from Employee where Emp_Id = 2;")
print "Total number of rows deleted :", conn.total_changes
c.execute("SELECT Emp_Id, Emp_Name, Salary, MobileNo from Employee")
for row in c:
   print "Emp_Id = ", row[0]
   print "Emp_Name = ", row[1]
   print "Salary = ", row[2]
   print "MobileNo = ", row[3], "\n"
print "Deletion done successfully";
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
