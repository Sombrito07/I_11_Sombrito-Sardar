import csv

department_fields = ['DEPARTMENT ID', 'DEPARTMENT NAME', 'LIST OF BATCHES']
department_database = 'DEPARTMENT.csv'

def add_department():
    print("-------------------------")
    print("Add Depatment Information")
    print("-------------------------")
    global department_fields
    global department_database


    department_data = []
    for field in department_fields:
        value = input("Enter " + field + ": ")
        department_data.append(value)

    with open(department_database, "a", encoding="utf-8") as fob:
        writer = csv.writer(fob)
        writer.writerows([department_data])

    print("Data saved successfully")
    Cont=input("Do you want to continue(Y/N):")
    if Cont=="Y":
        return option()
    else:
        exit

def display_batches():
    global department_database
    with open(department_database, "r", encoding="utf-8") as fob:
        reader = csv.reader(fob)
        for row in reader:
            if len(row)>0:
                print (row[2])
def option():
    print("DEPARTMENT MODULE FUNCTIONS")
    print("1.Create New Department")
    print("2.List of Batches")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_department()
    elif choice==2:
        display_batches()
    else:
        print("Invalid choice")
option() 


    
                         



