def count_operations(nums):
    nums=list(nums) #Convert tuple to list for easier modification
    operations=0
    while nums:
       if nums[0]==min(nums):
          nums.pop(0) #Remove first element
       else:
          nums.append(nums.pop(0)) #move first element to end
       operations=+1
       return operations
#Get input from user
nums=tuple(map(int,input("Enter distinct intergers separated by space:").split()))
print("Number of operations:",count_operations(nums))
