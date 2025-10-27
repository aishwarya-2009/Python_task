a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Equilateral triangle")
    elif a==b or b==c or a==c:
        print("Isosceles triangle")
    else:
        print("scalene triangle")
else:
        print("Not a valid triangle")
    
