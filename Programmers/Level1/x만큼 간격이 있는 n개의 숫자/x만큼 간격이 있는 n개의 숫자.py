def solution(x, n):
    answer = []
    i = 0
    num = x
    
    while i < n:
        i += 1
        answer.append(num)
        num += x
    return answer
