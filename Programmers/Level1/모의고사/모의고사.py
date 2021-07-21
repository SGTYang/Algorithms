def solution(answers):
    answer = []
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    tmp = [check(answers, one), check(answers, two), check(answers, three)]
    
    for i,k in enumerate(tmp):
        if k == max(check(answers, one), check(answers, two), check(answers, three)):
            answer.append(i+1)
        
    return answer

def check(answers, nums):
    i = 0
    k = 0
    total_sum = 0

    while i < len(answers):
        if answers[i] == nums[k]: 
            total_sum += 1
            
        k += 1
        
        if k == len(nums):
            k = 0
            
        i += 1
    
    return total_sum
