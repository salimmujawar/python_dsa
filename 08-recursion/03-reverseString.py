#reverse a given string with Recursion
#I/P: "john": O/P: "nhoj"

def recursiveStringReverse(str, strLen):    
    if strLen == 0:
        return str[0]
    print(str[strLen-1])
    return recursiveStringReverse(str[strLen-1], strLen-1)
    # print(strLen)
    # if strLen == 0:
    #     return str[0]
    # return recursiveStringReverse(str[strLen-1], strLen - 1)

# print(recursiveStringReverse("john",4))
recursiveStringReverse("john", 4)