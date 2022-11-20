#bubble sort, given an array sort
#i/p: arr = [5,8,3,9,7], o/p = [3,5,7,8,9]
#time compexity: O(n^2), space complexity: O(1)

def bubbleSort(nums):
    for i in range(len(nums) - 1):        
        for j in range(len(nums) -1):
            if nums[j] > nums[j+1]:
                #swap
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return nums

print(bubbleSort([5,8,3,9,7]))
