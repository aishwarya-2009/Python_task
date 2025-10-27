import cmath
#To handle both real and complex roots
#input coefficients
a=float(input("enter coefficient a:"))
b=float(input("enter coefficient b:"))
c=float(input("enter coefficient c:"))
#calculate discriminate
D=b**2-4*a*c
#compute roots using quadratic formula
root1=(-b+cmath.sqrt(D))/(2*a)
root2=(-b-cmath.sqrt(D))/(2*a)
#display result
print(f"\nDiscriminate (D)={D}")
#check nature of roots
if D>0:
  print("The roots are real and distinct.")
elif D==0:
  print("The roots are real and equal.")
else:
  print("The roots are complex.")
#Display roots
print(f"Root1={root1}")
print(f"Root2={root2}")

