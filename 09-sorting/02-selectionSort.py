#Slection Sort, here we look for smallest item in the list 
#and swap it out
#i/p: nums = [5,2,6,9,3,1,4,0,7,8], o/p: [0,1,2,3,4,5,6,7,8,9]
#time complexity: O(n^2), space complexity: O(1)

def selectionSort(nums):    
    for i in range(len(nums)):
        #set currrent index    
        min = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                #update min
                min = j
        #swap
        nums[i],nums[min] = nums[min], nums[i]
    return nums

print(selectionSort([5,2,6,9,3,1,4,0,7,8]))