def solution(n):
    ans = 1
    
    moves = 1
    
    while 1:
        if n ==1:
            return ans
        elif n%2 !=0:
            ans +=1
            n-=1
        else:
            n = n//2

    return ans
