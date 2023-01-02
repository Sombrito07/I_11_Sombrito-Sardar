import csv
import sys

course_fields = ['Course ID', 'Course Name','Marks Obtained(StudentID:Marks-StudentID:Marks-….)']
course_database = 'COURSE.csv' 
def add_course():
    print("-------------------------")
    print("Create New Course")
    print("-------------------------")
    global course_fields
    global course_database
      
    course_data = []
    for field in course_fields:
        value = input("Enter " + field + ": ")
        course_data.append(value)
    with open(course_database, "a", encoding="utf-8") as fob:
           writer=csv.writer(fob) 
           writer.writerows([course_data])

    print("New Course saved successfully")
    Cont=input("Do you want to continue(Y/N):")
    if Cont=="Y":
        return option()
    else:
        exit

def display():
    global course_database
    with open(course_database, "r", encoding="utf-8") as fob:
        reader = csv.reader(fob)
        for row in reader:
            if len(row)>0:
                print (row[2])
def grade(num):
    if num>=90:
        return("Outstanding Performance... You have passed the exam with grade A.")
    elif num<90 and num>=80:
        return("Excellent Performance... You have passed the exam with grade B.")
    elif num<80 and num>=70:
        return("Good Performance... You have passed the exam with grade C.")
    elif num<70 and num>=60:
        return("Your performance is average... Work hard... You have passed the exam with grade D.")
    elif num<60 and num>=50:
        return("Your performance is below average... There is massive scope of improvement... You have barely passed the exam with grade E.")
    else:
        return("Extremely poor performance... You have Failed the Exam and got F.")


def histogram():
    from matplotlib import pyplot as plt
    color_lst=['#C70039','#9BB1F2','#FFC300','#FF5733','#DAAFB1','#86B7C8']
    fig, ax = plt.subplots()
    legend_properties = {'weight':'heavy'}
    ax.set_facecolor("Black")
    ax.tick_params(axis="both", colors="white")
    fig.set_facecolor("Black")
    ax.set_xlabel('Grades--------->', color="white")
    ax.set_ylabel('No. of Students--------->', color="white")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.xaxis.label.set_weight("heavy")
    ax.yaxis.label.set_weight("heavy")
    count=0
    with open('COURSE.csv','r')as f:
        script= csv.reader(f)
        rows=[row for row in script]
        req=[]
        for i in range(len(rows)):
            if i==0:
                pass
            else:
                req+=[rows[i-1][2]]
        lst=[['Signal and System',(req[0].split('-'))[0:-1]],
             ['Analog Signals',(req[1].split('-'))[0:-1]],
             ['Python programing',(req[2].split('-'))[0:-1]]]

        for i in range(len(lst)):
            for j in range(len(lst[i][1])):
                try:
                    lst[i][1][j]=grade(int((lst[i][1][j].split(':'))[-1]))[-2]
                except:
                    lst[i][1][j]=''

        for k in range(2):
            a=lst[k][1].count('A')
            b=lst[k][1].count('B')
            c=lst[k][1].count('C')
            d=lst[k][1].count('D')
            e=lst[k][1].count('E')
            f=lst[k][1].count('F')
            lst[k][1]={'A':a,'B':b,'C':c,'D':d,'E':e,'F':f}

        for j in lst:
            x=list(j[1].keys())
            y=list(j[1].values())
            ax.plot(x, y,marker=",",color=color_lst[count],label=j[0],linewidth=3)
            leg=plt.legend(fontsize=10,loc="upper right", facecolor="Black",edgecolor="Black",prop=legend_properties)
            count+=1

        for text in leg.get_texts():
            text.set_color('White')

        plt.show()
def option():
    print("COURSE MODULE FUNCTIONS")
    print("1.Create New Course")
    print("2.Performance of students in Course")
    print("3.Course statistics as Histogram")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_course()
    elif choice==2:
        display()
    elif choice==3:
        histogram()   
    else:
        print("Invalid choice")
option()
  
