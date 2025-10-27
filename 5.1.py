def sortedSquares(nums):
    n=len(nums)
    res=[0]*n
    l,r=0,n-1
    pos=n-1 #fill from end
    while l<=r:
        if abs(nums[l])>abs(nums[r]):
            res[pos]=nums[l]*nums[l]
            l+=1
        else:
            res[pos]=nums[r]*nums[r]
            r-=1
        pos-=1
    return res
#-----Function calling & printing--------
nums1=[-4,-1,0,3,10]
nums2=[-7,-3,2,3,11]
print("input:",nums1)
print("output:",sortedSquares(nums1))
print("\ninput:",nums2)
print("output:",sortedSquares(nums2))
