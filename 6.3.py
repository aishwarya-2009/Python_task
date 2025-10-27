import csv
reader=csv.reader(open("students.csv"))
for row in reader:
    print(row)
