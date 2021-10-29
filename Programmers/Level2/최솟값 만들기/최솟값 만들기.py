def solution(A,B):
    answer = 0
    
    a = sorted(A)
    b = sorted(B, reverse=True)
    
    for i in range(len(a)):
        answer += a[i]*b[i]

    return answer
