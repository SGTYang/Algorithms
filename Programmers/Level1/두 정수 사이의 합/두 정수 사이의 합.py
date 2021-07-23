def solution(a, b):
  
    answer = 0
    
    if a > b:
        tmp = b
        b = a
        a = tmp
        
    for i in range(a,b+1):
        answer += i
        
    return answer
