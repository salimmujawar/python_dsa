#Check if an Array is Sorted

#Input Array

#numArr = [8,12,15] #O/P: Yes
#numArr = [8,10,10,12] #O/P: Yes
#numArr = [100] #O/P: Yes
numArr = [100,20,200] #O/P: No

#Time Complexity: O(n)
def isSorted(numArr):
  for i in range(1, len(numArr)):
    if numArr[i] < numArr[i-1]:
      return False
  return True


print(isSorted(numArr))      
