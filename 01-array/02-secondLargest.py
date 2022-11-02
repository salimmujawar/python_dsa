#Test Cases

#numArr = [10,5,8,20]
numArr = [1,1,1,1] #O/P: -1
#numArr = [20,10,20,8,12]
#numArr = [20,10,20,12,8] 

#Time Complexity: O(n)  

def findSecondLargest(arrNum):
  maxVal = -1;
  secVal = -1;
  for x in arrNum:
    if x > maxVal:
      maxVal = x;     
    #Current val less than max, and curr val is greater than secVal 
    if x < maxVal and x > secVal:
      secVal = x;
  if (secVal > -1):
    return arrNum.index(secVal)  
  else:
    return secVal



print(findSecondLargest(numArr))
