#Check if an Array is Sorted

#Input Array

#numArr = [0,0,1,1,1,2,2,3,3,4] #O/P: [0,1,2,3,_,_,_,_,_,_], s=4
numArr = [10,20,20,30,30,30] #O/P: [10,20,30,_,_,_], s=3
#numArr = [10,10,10] #O/P: [10,_,_], s=1

#Time Complexity: O(n)
def removeDuplicates(arr):
    left = 1
    for right in range(1, len(arr)):
        if arr[left] != arr[right -1]:
            arr[left] = arr[right]
            left += 1
    return left

print(int(removeDuplicates(numArr)))