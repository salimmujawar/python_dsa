#Given an array tell the first recurring char
#arr = [2,5,1,2,3,5,1,2,4], O/P: 2

numsArr = [2,5,1,2,3,5,1,2,4]

def recurringCharacter(arr):
    preMap = {}
    for i in range(len(arr)):
        if preMap.get(arr[i]):
            return arr[i]
        else:
           preMap[arr[i]] = 1 
           
print(recurringCharacter(numsArr))
