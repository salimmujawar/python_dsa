#Stock Buy and Sell Problem

#Input Array

numArr = [1,5,3,8,12] #O/P: 13
#numArr = [30,20,10] #O/P: 0
#numArr = [1,5,3,1,2,8] #O/P: 11

#Time Complexity O(n)
def buyAndSell(arr):
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:            
            profit += (arr[i] - arr[i-1])
    return profit

print(buyAndSell(numArr))