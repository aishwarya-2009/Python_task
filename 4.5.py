students={}
n=int(input("Enter number of students:"))
for _ in range(n) :
    name=input("\Enter student name:")
    test=float(input("Enter Test mark:"))
    assignment=float(input("Enter Assignment mark:"))
    lab=float(input("enter lab mark:"))
    students[name]=[test,assignment,lab]
#Function to calculate average
def average(marks):
    return sum(marks)/len(marks)
#1.Highest average score
max_avg=max(average(marks) for marks in students.values())
highest_avg_students=[name for name,marks in students.items() if average(marks)==max_avg]
#.Highest assignment marks
max_assignment=max(marks[1] for marks in students.values())
highest_assignment_students=[name for name,marks in students.items() if marks[1]==max_assignment]
#3.Lowest lab marks
min_lab=min(marks[2] for marks in students.values())
lowest_lab_students=[name for name,marks in students.items() if marks[2]==min_lab]
#4.Lowest average score
min_avg=min(average(marks) for marks in students.values())
lowest_avg_students=[name for name,marks in students.items() if average(marks)==min_avg]
#Display result
print("\n---Result---")
print("Highest average score:",highest_avg_students,"with average=",max_avg)
print("Highest assignment marks:",highest_assignment_students,"with marks=",max_assignment)
print("Lowest lab marks:",lowest_lab_students,"with marks=",min_lab)
print("Lowest average score:",lowest_avg_students,"with average=",min_avg)
