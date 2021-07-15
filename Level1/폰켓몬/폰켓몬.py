def solution(nums):
    answer = 0
    
    a = len(nums)//2
    
    list = []
    
    for i in nums:
        if len(list)<a:
            if i not in list:
                list.append(i)
        else:
            break
            
    answer = len(list)
    
    return answer
