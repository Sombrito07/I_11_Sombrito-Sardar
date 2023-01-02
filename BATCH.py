import csv

batch_fields = ['BATCH ID', 'BATCH NAME', 'DEPARTMENT NAME', 'LIST OF COURSES', 'LIST OF STUDENTS']
batch_database = 'BATCH.csv'

def add_batch():
    print("-------------------------")
    print("Add Batch Information")
    print("-------------------------")
    global batch_fields
    global batch_database


    batch_data = []
    for field in batch_fields:
        value = input("Enter " + field + ": ")
        batch_data.append(value)

    with open(batch_database, "a", encoding="utf-8") as fob:
        writer = csv.writer(fob)
        writer.writerows([batch_data])

    print("Data saved successfully")
    Cont=input("Do you want to continue(Y/N):")
    if Cont=="Y":
        return option()
    else:
        exit

def display_students():
    global batch_database
    with open(batch_database, "r", encoding="utf-8") as fob:
        reader = csv.reader(fob)
        for row in reader:
            if len(row)>0:
                print (row[4])
def display_course():
    global batch_database
    with open(batch_database, "r", encoding="utf-8") as fob:
        reader = csv.reader(fob)
        for row in reader:
            if len(row)>0:
                print (row[3])

def plot():
    from matplotlib import pyplot as plt
    import numpy as np 
    with open("REPORTCARD.txt",'r') as fob:
        student=[]
        percent=[]
        for line in fob:
            word=line.split(" ")
            student.append(word[0])
            percent.append(word[-2])
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(percent, labels=student, autopct='%.1f%%')
        ax.set_title('Sport Popularity')
        plt.tight_layout()
        plt.show()
def option():
    print("BATCH MODULE FUNCTIONS")
    print("1.Create New Batch")
    print("2.List of students in batch")
    print("3.List of courses in batch")
    print("4.Batch Statistics in pie plot")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_batch()
    elif choice==2:
        display_students()
    elif choice==3:
        display_course()
    elif choice==4:
        plot() 
    else:
        print("Invalid choice")
option()
  

    
