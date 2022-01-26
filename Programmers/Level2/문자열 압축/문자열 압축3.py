def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        compare = s[:i]
        tmp = ''
        cnt = 1
        rest=len(s)%i
        for j in range(i,len(s)-len(s)%i,i):
            if compare == s[j:i+j]:
                cnt += 1
            else:
                if cnt >= 2:
                    tmp+= str(cnt)+compare
                    cnt = 1
                    compare = s[j:i+j]
                else:
                    tmp += compare
                    compare = s[j:i+j]
                    
        if cnt >=2:
            tmp += str(cnt)+compare
        else:
            tmp += compare
            
        if rest !=0:
            answer.append(len(tmp+s[-rest:]))
        else:
            answer.append(len(tmp))
    return min(answer)
