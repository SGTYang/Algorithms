def solution(dartResult):
    answer = 0
    tmp = ""
    arry = []
    sum_arry = []
    for i in range(len(dartResult)-1):
        if not dartResult[i].isdigit() and dartResult[i+1].isdigit():
            tmp += dartResult[i]
            arry.append(tmp)
            tmp = ""
        else:
            tmp += dartResult[i]
    tmp += dartResult[-1]
    arry.append(tmp)
    
    for i in range(len(arry)):
        tmp_sum = int(arry[i][0])
        if arry[i][1] == "0":
            tmp_sum = 10
        for j in range(1,len(arry[i])):
            if arry[i][j] == "S":
                tmp_sum = tmp_sum**1
            elif arry[i][j] == "D":
                tmp_sum = tmp_sum**2
            elif arry[i][j] == "T":
                tmp_sum = tmp_sum**3
            elif arry[i][j] == "*":
                if i > 0:
                    sum_arry[i-1] = sum_arry[i-1]*2
                tmp_sum = tmp_sum*2
            elif arry[i][j] == "#":
                tmp_sum = tmp_sum*(-1)
        sum_arry.append(tmp_sum)
    answer = sum(sum_arry)
        
    return answer
