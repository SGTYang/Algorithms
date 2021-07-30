def solution(s):
    answer = len(s)
    print("length: {}".format(len(s)))
    for i in range(1, len(s)//2+1):
        string = ""
        tmp_arry = []
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s)-len(s)%i+1, i):
            if tmp != s[j:j+i]:
                if cnt > 1:
                    tmp_arry.append(str(cnt)+tmp)
                    cnt = 1
                    tmp = s[j:j+i]
                else:
                    tmp_arry.append(tmp)
                    tmp = s[j:j+i]
            else:
                cnt += 1
            
        if len(s)%i > 0:
            tmp_arry.append(s[-(len(s)%i):])
        answer = min(answer, len("".join(tmp_arry)))
                     
    return answer
