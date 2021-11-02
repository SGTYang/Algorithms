def solution(n, t, m, p):
    answer = []
    arry = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    s = 0
    comb = ''
    
    def conv(n, base):
        n, rest = divmod(n,base)
        if n ==0:
            return arry[rest]
        else:
            return conv(n, base)+arry[rest]
    
    while len(comb) < t*m:
        comb+=conv(s,n)
        s += 1
    
    for i in range(0,len(comb)):
        answer.append(comb[i])

    return "".join(answer[p-1::m][:t])
