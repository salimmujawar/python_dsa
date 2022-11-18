#Check if duplicate exist
def checkDuplicate(nums):
    nums_dict = {}
    for i in range(len(nums)):
        if nums_dict.get(nums[i]) == nums[i]:
            return True
        else:
            nums_dict[nums[i]] = nums[i]
    return False


print(checkDuplicate([3,3]))