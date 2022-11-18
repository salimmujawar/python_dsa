#find factorial of any given number
#i/p= 5!, o/p = 120
#time complexity: O(n)

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))