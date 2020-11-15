# import math
# k = 31


# def check(k):
#     for i in range(2, int(math.sqrt(k))):
#         if k % i == 0:
#             print("False")
#             return
#     print("True")


def twoSum(nums, target):
    h = {}
    for i, n in enumerate(nums):
        value = target - n
        if value in h:
            return [i, h[value]]
        h[n] = i

def twoSum(nums, target):
    h = {}
    for i in range(len(nums)):
        value = target - nums[i]
        if value in h:
            return [i, h[value]]
        h[nums[i]] = i



x = -10
def reverse(x):
    if pow(-2,31) < x < pow(2,31):
        if x > 0:
            r = int(str(x)[::-1])
        else:
            s = str(x)[1:]
            r = int(s[::-1])*-1
        if pow(-2,31) < r < pow(2,31):
            return r
    return 0

#reverse(x)

def isPalindrome(x: int) -> bool:
    if x < 0:
        return 0
    strX = str(x)
    strLen = len(strX)
    if strLen == 1:
        return 1
    if strLen == 2:
        if strX[0] == srtX[1]:
            return 1
        else:
            return 0
    midl = int((strLen-(strLen % 2))/2)
    if strX[:midl] == strX[:midl:-1]:
        return 1
    return 0

pow(2,15)

x = 11
isPalindrome(x)
