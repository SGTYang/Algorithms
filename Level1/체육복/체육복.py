def solution(n, lost, reserve):
    answer = n
    
    rest = set(lost)-set(reserve)
    re_lost = set(lost)-set(reserve)
    ck_reserve = set(reserve) - set(lost)
    
    for i in (rest):
        if i-1 in ck_reserve:
            re_lost.remove(i)
            ck_reserve.remove(i-1)
        elif i+1 in ck_reserve:
            re_lost.remove(i)
            ck_reserve.remove(i+1)
            
    answer = n - len(re_lost)
    
    return answer
 
