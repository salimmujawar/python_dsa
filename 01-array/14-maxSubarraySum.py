#Max Sum of Subarray

#Input Array
numArr = [2,3,-8,7,-1,2,3] #O/P: 11
#numArr = [5,8,3] #O/P: 16
numArr = [-6,-1,-8] #O/P: -1

#Time Complexity O(n)
def max_sum_subarray(arr):  
  res = arr[0]
  max_ending = arr[0]

  for i in range(1, len(arr)):
    max_ending = max(max_ending+arr[i], arr[i])
    res = max(res, max_ending)
  
  return res;

print(max_sum_subarray(numArr))