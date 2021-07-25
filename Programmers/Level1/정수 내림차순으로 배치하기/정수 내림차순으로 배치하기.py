def solution(n):
    answer = 0
    
    n = list(str(n))
    n = sorted(n, reverse=True)
    
    return int("".join(n))
