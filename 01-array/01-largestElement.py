#Test Cases

#numArr = [10,5,8,20]
#numArr = [1,1,1,1]
#numArr = [20,10,20,8,12]
numArr = [20,10,20,12,8] 

#Time Complexity: O(n)
def largestElement(numArr):
    maxNum = -1;
    for x in numArr:
        if x > maxNum:
            maxNum = x;
    return maxNum;

print(largestElement([4,3,9,8]));