num=int(input("Enter a number:"))

square=num*num
digits=len(str(num))
last_digits=square % (10 ** digits)

if last_digits==num:
    print(num,"is an automorphic number")
else:
    print(num,"is not an automorphic number")
