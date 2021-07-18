import math
def solution(nums):

    answer = 0
    arry = []

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                arry.append(nums[i]+nums[j]+nums[k])

    for i in range(len(arry)):
        if prime(arry[i]):
            answer+=1

    return answer

def prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            return False 
    return True

