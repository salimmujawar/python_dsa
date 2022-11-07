#Trap Rain Water

#Input Array

numArr = [5,0,6,2,3] #O/P: 6
#numArr = [3,0,1,2,5] #O/P: 6
#numArr = [2,0,2] #O/P: 2
#numArr = [1,2,3] #O/P: 0
#numArr = [3,2,1] #O/P: 0

#Time Complexity O(n)
def trap_rain_water(arr):
  if not arr: return 0

  arr_len = len(arr)
  #2 pointers left, right
  l,r = 0, arr_len-1
  #left and right arr
  lmax, rmax = arr[l], arr[r]
  res = 0

  while l < r :  
    if lmax < rmax:  
      l += 1
      lmax = max(lmax, arr[l])
      res += lmax - arr[l]
    else:
      r -= 1
      rmax = max(rmax, arr[r])
      res += rmax - arr[r]
  return res

print(trap_rain_water(numArr))

