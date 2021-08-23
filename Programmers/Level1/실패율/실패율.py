def solution(N, stages):
    answer = []
    arry = {}
    pp = len(stages)
    for i in range(1,N+1):
        tmp = stages.count(i)
        if pp != 0:    
            arry[i] = tmp/pp
        else:
            arry[i] = 0
        pp = pp - tmp
    answer = [i[0] for i in sorted(arry.items(), key= lambda x:x[1], reverse=True)]
    return answer
