#Left Rotate By One

#Input Array

numArr = [1,2,3,4,5] #O/P: [2,3,4,5,1]
#numArr = [30,5,20] #O/P: [5,20,30] 

def rotateKTimes(arr, k):
  for i in range(k):
    arr = rotateLeft(arr)
  return arr

#Time Complexity: O(n)
def rotateLeft(arr):
  tmp = arr[0]
  n = len(arr)
  for i in range(1, n ):
    arr[i-1] = arr[i]
  arr[n-1] = tmp
  return arr


print(rotateLeft(numArr))
#print(rotateKTimes(numArr, 2))