def find_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
#Get input from user
nums=list(map(int,input("enter numbers separated by space:").split()))
duplicate=find_duplicate (nums)
print("The repeated number is:",duplicate)
