def solution(s):
    answer = []
    num = []
    tmp_arry = []
    tmp = ''
    for i in range(1,len(s)-1):
        if s[i].isdigit():
            tmp += s[i]
        if s[i].isdigit() and s[i+1] ==',' or s[i+1] == '}':
            if len(tmp) != 0:
                tmp_arry.append(tmp)
                tmp = ''
        if (s[i-1] == '}' and s[i] ==',' and s[i+1] =='{') or i == len(s)-2:
            if len(tmp_arry) != 0:
                num.append(tmp_arry)
                tmp_arry = []
    num = sorted(num, key=len)

    for i in range(len(num)):
        for j in range(len(num[i])):
            if int(num[i][j]) not in answer:
                answer.append(int(num[i][j]))
    return answer
