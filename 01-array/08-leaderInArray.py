#Find Leader in an Array, all element to right of it should be small

#Input Array

numArr = [15,18,5,3,6,2] #O/P: [2,6,18]
numArr = [10,20,30] #O/P: [30]
numArr = [30,20,10] #O/P: [10,20,30]

#Time Complexity: O(n)
def leaderInArray(arr):
    n = len(arr)
    current_leader = arr[n-1]
    i = n-2
    print(current_leader)
    while (i > -1):
        if arr[i] > current_leader:
            current_leader = arr[i]
            print(current_leader)    
        i -= 1    

leaderInArray(numArr)