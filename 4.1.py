def SmallestCommonElement(mat):
    from bisect import bisect_left

    rows = len(mat)
    cols = len(mat[0])

    # Check each number in the first row
    for num in mat[0]:
        found = True
        for r in range(1, rows):
            # Binary search in the current row
            left, right = 0, cols - 1
            while left <= right:
                mid = (left + right) // 2
                if mat[r][mid] == num:
                    break
                elif mat[r][mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                found = False
                break
        if found:
            return num

    return -1  # Return -1 if no common element is found
rows= int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
mat=[]
print("Enter matrix values row by row (sorted in increasing order):")
for _ in range(rows):
    row=list(map(int,input().split()))
    mat.append(row)
#Find and display smallest common element
result=SmallestCommonElement(mat)
print("Smallest common element in all rows:",result)


