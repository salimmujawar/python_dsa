#Find Longest Odd Sub Array

#Input
arr = [5,10,20,6,3,8] # O/P: [3]

def longestEvenOddSubArray(arr):
  maxSum = 1;
  currSum = 1;
  for i in range(len(arr)):
    if ((arr[i]%2 == 0) and (arr[i-1]%2 != 0) or
        ((arr[i]%2 != 0) and (arr[i-1]%2 == 0))):
          currSum += 1
          maxSum = max(maxSum, currSum)
    else:
      currSum = 1    
  return maxSum

print(longestEvenOddSubArray(arr))