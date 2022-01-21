Employee = dict()

def AddNewEmployee():
	
	ID = input("Enter the employee ID : ")
	if ID in Employee:
		print("Sorry this ID is already exist")
	else :
		NAME = input("Enter the employee Name : ")
		JOB = input("Enter the employee Job : ")
		SALARY = input("Enter the employee Salary : ")
		
		Employee[ID] ={}
		Employee[ID]['NAME'] = NAME
		Employee[ID]['JOB'] = JOB
		Employee[ID]['SALARY'] = SALARY
		
	print(Employee)
	
def RemoveEmployee():

	ID = input("Enter the employee ID : ")
	
	if ID not in Employee:
		print("Sorry this ID is not exist")
	else :
		Employee.pop(ID)
		
	print(Employee)

def PrintEmployee():	
	
	ID = input("Enter the employee ID : ")
	
	if ID not in Employee:
		print("Sorry this ID is not exist")
	else :
		print(Employee[ID])
		
def PrintSpecEmployeeData():	
	
	ID = input("Enter the employee ID : ")
	
	if ID not in Employee:
		print("Sorry this ID is not exist")
		
	else :
		SpecData = input("Enter the specific Data you want : ")
		SpecData = SpecData.lower()
		
		if SpecData == "name":
			print("Employee with ID " + ID + " Name : " + Employee[ID]['NAME'])
		
		elif SpecData == "job":
			print("Employee with ID " + ID + " Job : " + Employee[ID]['JOB'])
		
		elif SpecData == "salary":
			print("Employee with ID " + ID + " Salary : " + Employee[ID]['SALARY'])
		
		else:
			print("Sorry this is Data like this")


