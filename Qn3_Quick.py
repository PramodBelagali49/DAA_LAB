import timeit
def quick_sort(arr,low,high):
    if low<high :
        pivotIndx=partition(arr,low,high)
        quick_sort(arr,low,pivotIndx-1)
        quick_sort(arr,pivotIndx+1,high)
    return arr

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    for j in range(low+1,high+1):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[low]=arr[low],arr[i]
    return i

arr=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    arr.append(int(input("Enter element:")))
print("Original array:",arr)

time_taken = timeit.timeit(lambda: quick_sort(arr,0,n-1), number=1)

print("Sorted array:", quick_sort(arr,0,n-1))
print(f"Time taken: {time_taken*1000} ms")


