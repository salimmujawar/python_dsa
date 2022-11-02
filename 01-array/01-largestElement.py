def largestElement(numArr):
    maxNum = 0;
    for x in numArr:
        if x > maxNum:
            maxNum = x;
    return maxNum;

print(largestElement([4,3,9,8]));