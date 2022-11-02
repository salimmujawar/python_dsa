#Check if an Array is Sorted

#Input Array

#numArr = [10,5,7,30] #O/P: [30,7,5,10]
#numArr = [30,20,5] #O/P: [5,20,30]
numArr = [30,7,6,5,10] #O/P: [10,5,6,7,30]

#Time Complexity: O(n)
def reverseArray(numArr):
  leftIdx = 0
  rightIdx = len(numArr) - 1
  tmp = 0;
  while (leftIdx < rightIdx):
    tmp = numArr[rightIdx]
    numArr[rightIdx] = numArr[leftIdx]
    numArr[leftIdx] = tmp
    leftIdx += 1;
    rightIdx -= 1;
  return numArr

print(reverseArray(numArr))