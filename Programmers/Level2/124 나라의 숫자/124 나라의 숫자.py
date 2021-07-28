def solution(n):
    answer = ''
    while(n > 0):
        remainder = n%3
        
        if remainder == 0:
            remainder = 4
        answer = str(remainder)+answer

        n = (n-1)//3
    
    return answer
