#Max Sum of Subarray

#Input Array
numArr = [2,3,-8,7,-1,2,3] #O/P: 11
#numArr = [5,8,3] #O/P: 16
#numArr = [-6,-1,-8] #O/P: -1

#Time Complexity O(n)
def max_sum_subarray(arr):  
  maxSum = 0
  curSum = 0
  
  #Here we Use Kadane's algo
  for i in range(len(arr)):  
    #we check which is max (cur_sum + cur_ele, cur_ele)  
    curSum = max(curSum + arr[i], arr[i])
    #In max_sum we keep, max of max_sum / cur_sum
    maxSum = max(maxSum, curSum)
  
  return maxSum;

print(max_sum_subarray(numArr))