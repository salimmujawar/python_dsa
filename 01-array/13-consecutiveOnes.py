#Consecutive One's in an Binary Array

#Input Array
numArr = [0,1,1,0,1,0] #O/P: 2
#numArr = [1,0,1,1,1,1,0,1,1] #O/P: 4
#numArr = [1,1,1,1] #O/P: 4
#numArr = [0,0,0] #O/P: 0

#Time Complexity O(n)
def max_ones(arr):
  max_ones = 0
  count = 0
  for i in range(len(arr)):
    if arr[i] == 0:
      count = 0
    else:
      count += 1
      max_ones = max(count, max_ones)
      
  return max_ones

print(max_ones(numArr))