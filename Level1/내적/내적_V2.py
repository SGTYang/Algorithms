def solution(a, b):
    answer = 0
    
    for i in range(0, len(a)//2):
        answer+=a[i]*b[i]
        answer+=a[i+len(a)//2]*b[i+len(a)//2]

    if(len(a)%2 != 0):
        answer+=a[-1]*b[-1]
    
    return answer
