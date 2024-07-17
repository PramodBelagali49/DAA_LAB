# import time
import timeit

def merge_sort(arr):

    if(len(arr)<=1):
        return arr
    
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]

    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)
    return merge(left_arr,right_arr)

def merge(left_arr,right_arr):
    i=0
    j=0
    merged_arr=[]
    while(i<len(left_arr) and j<len(right_arr)): 
        if left_arr[i]<right_arr[j]:
            merged_arr.append(left_arr[i])
            i=i+1
        else:
            merged_arr.append(right_arr[j])
            j+=1
    while (i<len(left_arr)):
        merged_arr.append(left_arr[i])
        i=i+1
    while (j<len(right_arr)) :
        merged_arr.append(right_arr[j])
        j=j+1
    return merged_arr

n=int(input("Enter the size of the array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element:")))
print("Original array:",arr)

# start=time.time()
# arr=merge_sort(arr)
# end=time.time()

# print("Sorted array:",arr)
# print(f"Time taken:{(end-start)*1000}")

time_taken = timeit.timeit(lambda: merge_sort(arr), number=1)

print("Sorted array:", merge_sort(arr))
print(f"Time taken: {time_taken*1000} ms")
