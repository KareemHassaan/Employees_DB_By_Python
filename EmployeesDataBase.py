import DictOperations
from DictOperations import AddNewEmployee,RemoveEmployee,PrintEmployee,PrintSpecEmployeeData

while(1):
	#Scanning from the user the operation that he want
	operation = int(input('''	|***************** Company Database *****************|
	|Enter (1) to Add new employee                       |
	|Enter (2) to Remove employee from the system        |
	|Enter (3) to Print employee data                    |
	|Enter (4) to Print one of specific employee data    |
	|****************************************************|\n'''))

	if operation == 1:
		AddNewEmployee()
	
	elif operation == 2:
		RemoveEmployee()
		
	elif operation == 3:
		PrintEmployee()
		
	elif operation == 4:
		PrintSpecEmployeeData()

	else :
		print("Sorry this option is unavailable")