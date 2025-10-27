def bubble_sort(arr):
    n=len(arr)
    #Traverse through all elements
    for i in range(n):
        #Last elements are already sorted
        for j in range(0,n-i-1):
            #swap if the elements found is greater than next
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
#-----main program------
n=int(input("Enter number of elements:"))
arr=list(map(int,input("Enter the elements:").split()))
sorted_arr=bubble_sort(arr)
print("sorted list:",sorted_arr)
        
