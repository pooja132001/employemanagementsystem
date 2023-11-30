# importing mysql connector
import mysql.connector


con = mysql.connector.connect(
	host="localhost", user="root", password="Pooja@123", database="emp")

# Function to mAdd_Employee
def Add_Employ():

	empID = input("Enter Employee Id : ")
	
	# Checking if Employee with given Id 
	# Already Exist or Not
	if(check_employee(empID) == True):
		print("Employee already exists\nTry Again\n")
		menu()
		
	else:
		empname = input("Enter Employee Name : ")
		emppost = input("Enter Employee Post : ")
		empsalary = input("Enter Employee Salary : ")
		data = (empID, empname, emppost, empsalary)
	
		# Inserting Employee details in 
		# the Employee Table
		sql = 'insert into employee values(%s,%s,%s,%s)'
		c = con.cursor()
		
		# Executing the SQL Query
		c.execute(sql, data)
		
		# commit() method to make changes in
		# the table
		con.commit()
		print("Employee Added Successfully ")
		menu()

# Function to Promote Employee
def Promote_Employee():
	empID = int(input("Enter Employ's Id"))
	
	# Checking if Employee with given Id 
	# Exist or Not
	if(check_employee(empID) == False):
		print("Employee does not exists\nTry Again\n")
		menu()
	else:
		Amount = int(input("Enter increase in Salary"))
		
		# Query to Fetch Salary of Employee 
		# with given Id
		sql = 'select empsalary from employee where empID=%s'
		data = (empID,)
		c = con.cursor()
		
		# Executing the SQL Query
		c.execute(sql, data)
		
		# Fetching Salary of Employee with given Id
		r = c.fetchone()
		t = r[0]+Amount
		
		# Query to Update Salary of Employee with
		# given Id
		sql = 'update employee set empsalary=%s where empID=%s'
		d = (t, empID)
		
		# Executing the SQL Query
		c.execute(sql, d)
		
		# commit() method to make changes in the table
		con.commit()
		print("Employee Promoted")
		menu()

# Function to Remove Employee with given Id
def Remove_Employ():
	empID = input("Enter Employee Id : ")
	
	# Checking if Employee with given Id Exist
	# or Not
	if(check_employee(empID) == False):
		print("Employee does not exists\nTry Again\n")
		menu()
	else:
		
		# Query to Delete Employee from Table
		sql = 'delete from employee where empID=%s'
		data = (empID,)
		c = con.cursor()
		
		# Executing the SQL Query
		c.execute(sql, data)
		
		# commit() method to make changes in 
		# the table
		con.commit()
		print("Employee Removed")
		menu()


# Function To Check if Employee with
# given Id Exist or Not
def check_employee(employee_id):
	
	# Query to select all Rows f
	# rom employee Table
	sql = 'SELECT * FROM employee WHERE emp ID =%s'
	
	# making cursor buffered to make
	# rowcount method work properly
	c = con.cursor(buffered=True)
	data = (employee_id,)
	
	# Executing the SQL Query
	print("Executing SQL query:", sql, "with data:", data)
	c.execute(sql, data)
	
	# rowcount method to find
	# number of rows with given values
	r = c.rowcount
	if r == 1:
		return True
	else:
		return False

# Function to Display All Employees
# from Employee Table
def Display_Employees():
	
	# query to select all rows from 
	# Employee Table
	sql = 'select * from employee'
	c = con.cursor()
	
	# Executing the SQL Query
	c.execute(sql)
	
	# Fetching all details of all the
	# Employees
	r = c.fetchall()
	for i in r:
		print("Employee Id : ", i[0])
		print("Employee Name : ", i[1])
		print("Employee Post : ", i[2])
		print("Employee Salary : ", i[3])
		print("---------------------\
		-----------------------------\
		------------------------------\
		---------------------")
		
	menu()

# menu function to display menu
def menu():
	print("Welcome to Employee Management Record")
	print("Press ")
	print("1 to Add Employee")
	print("2 to Remove Employee ")
	print("3 to Promote Employee")
	print("4 to Display Employees")
	print("5 to Exit")

	ch = int(input("Enter your Choice "))
	if ch == 1:
		Add_Employ()
	elif ch == 2:
		Remove_Employ()
	elif ch == 3:
		Promote_Employee()
	elif ch == 4:
		Display_Employees()
	elif ch == 5:
		exit(0)
	else:
		print("Invalid Choice")
		menu()


# Calling menu function
menu()

