def solution(n):
    answer = 0
    n = list(str(n))
    n.reverse()
    n.sort()
    
    for i in range(len(n)):
        answer += int(n[i])*10**i
    return answer
