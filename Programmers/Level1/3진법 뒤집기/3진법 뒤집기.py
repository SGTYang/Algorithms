def solution(n):
    answer = 0
    arry = []
    if n < 3:
        return n
    
    while n > 0:
        arry.append(n%3)
        n = n//3

    for i in range(0,len(arry)):
        answer += (arry[len(arry)-1-i])*(3**i)
        
    return answer
