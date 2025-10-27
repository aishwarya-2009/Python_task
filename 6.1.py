file_name="example.txt" #your file
line_number=int(input("Enter the line number to delete:"))
with open(file_name,"r")as f:
    lines=f.readlines()
if 1<=line_number<=len(lines):
    del lines[line_number-1]
with open(file_name,"w")as f:
    f.writelines(lines)
print("Line deleted successfully")


