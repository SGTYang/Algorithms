def solution(n, m):
    answer = []
    
    if n < m:
        tmp = m
        m = n
        m =tmp
    
    max_num = 0
    
    for i in range(1, n+1):
        if m%i == 0 and n%i ==0:
            max_num = max(max_num,i)
    answer.append(max_num)
    
    for i in range(m, n*m+1,m):
        if i%n ==0 :
            answer.append(i)
            break
    return answer
