#Find Max diff in an Array, arr[j] - arr[i], such that j > i

#Input Array

numArr = [2,3,10,6,4,8,1] #O/P: 8
numArr = [10,20,30] #O/P: 20
numArr = [30,10,8,2] #O/P: -2

#Time Complexity O(n)
def max_diff(arr):
    res = arr[1]-arr[0]
    min_num = arr[0]
    for j in range(1, len(arr)):
        res = max(res, arr[j] - min_num)
        min_num = min(min_num, arr[j])
    return res

print(max_diff(numArr))

