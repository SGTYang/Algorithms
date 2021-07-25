import math
def solution(n):
    
    if (int(math.sqrt(n)))**2 == n:
        answer = (math.sqrt(n)+1)**2
    else:
        return -1
    return answer
