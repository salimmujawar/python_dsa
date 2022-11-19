# Given a number N return the index value of the fibonacci
# where sequence is:
# 0,1,1,2,3,5,8,13,21,34,55,89,144 ....
#fibonacci(n) = fib(n-1) + fib(n-2)
#Time complexity: O(2^N) exponential
#Iterative approch is O(n)

def fibonacci(num):
    if num < 2:
        return num
    return (fibonacci(num-1) + fibonacci(num-2))

print(fibonacci(0))