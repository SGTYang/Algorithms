def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 1
        tmp = 0
        for j in range(1, i//2 + 1):
            if i%j == 0:
                cnt += 1

        if cnt%2 != 0:
            tmp = i*(-1)
        else:
            tmp = i
            
        answer += tmp
        
    return answer
