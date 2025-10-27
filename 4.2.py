def countBits(n):
    ans=[]
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans
#get input from user
n=int=int(input("enter a non-negative integer:"))
result=countBits(n)
print("Count of 1's for numbers from 0 to",n,":",result)
