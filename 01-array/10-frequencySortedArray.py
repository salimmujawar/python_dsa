#Find Frequencies in a Sorted Array

#Input Array

numArr = [10,10,10,25,30,30] #O/P: 10=3,25=1,30=2
#numArr = [10,10,10] #O/P: 10=3
#numArr = [10,20,30] #O/P: 10=1,20=1,30=1

#Time Complexity O(n)
def frequencyOfNum(arr):
    curr_num = arr[0]
    num_count = 0
    for i in range(len(arr)):
        if arr[i] != curr_num:
            print(f"{curr_num} = {num_count}")
            curr_num = arr[i]
            num_count =1
        else:
           num_count +=1
    print(f"{curr_num} = {num_count}")
frequencyOfNum(numArr) 

