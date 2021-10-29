def solution(s):
    answer = ''
    
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = int(s[i])

    m = max(s)
    mi = min(s)
    answer = str(mi)+" "+str(m)
    return answer
