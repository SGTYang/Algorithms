import math
def solution(n):
    answer = 0
    
    if n == 2:
        return 1
    
    for i in range(2,n+1):
        check = True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                check = False
                break
        if check:
            answer += 1
                
    return answer
