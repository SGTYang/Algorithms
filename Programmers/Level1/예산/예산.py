def solution(d, budget):
    answer = 0
    d.sort()
    total_sum = 0
    
    for i in d:
        if total_sum+i <= budget:
            answer += 1
            total_sum += i
    return answer
