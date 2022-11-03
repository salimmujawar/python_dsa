#Move Zeros to End of Array

#Input Array

#numArr = [8,5,0,10,0,20] # O/P: [8,5,10,20,0,0]
numArr = [0,0,0,10,0] # O/P: [10,0,0,0,0]
#numArr = [10,20] # O/P: [10,20]

#Time Complexity: O(n)
def moveZerosToEnd(arr):
  #Maintain the nonzero Count
  nonZeroCount = 0
  tmp = 0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[nonZeroCount], arr[i] = arr[i], arr[nonZeroCount]      
      nonZeroCount += 1
  return arr

print(moveZerosToEnd(numArr))