import csv
def entermarks():
  a=input("Enter Course Name of Examination:")
  b=input("Enter all the Student's Roll number in list form:" )
  c=input("Enter respective marks of the students out of 100 in list form:")
  print("Data saved")
  Cont=input("Do you want to continue(Y/N):")
  if Cont=="Y":
    return option()
  else:
     exit
  x=[a,b,c]
  with open("EXAMINATION.csv" ,"a") as e:
      writer=csv.writer(e)
      writer.writerow(x)
  
    
def performance():
  with open("EXAMINATION.csv" ,"r") as e:
      r=csv.reader(e)
      for row in r:
        print(row)
  
  
    
def plot():
  import matplotlib.pyplot as plt
  import numpy as np
  x1 = np.array([1,2,3,4])
  y1 = np.array([90,92,88,89])
  x2 = np.array([1,2,3,4])
  y2 = np.array([85,89,100,96])
  plt.xlabel('Roll Number')
  plt.ylabel('Marks Obtained')
  plt.scatter(x1, y1, color='black')
  plt.scatter(x2, y2, color='red')
  plt.show()
def option():
  print("EXAMINATION MODULE FUNCTIONS")
  print("1.Enter Marks of Students")
  print("2.View Performance of Students")
  print("3.Exam Statistics in scatter plot")
  choice=int(input("Enter your choice:"))
  if choice==1:
    entermarks()
  elif choice==2:
    performance()
  elif choice==3:
    plot()
  else:
    print("Invalid choice")
option()  


    
                         