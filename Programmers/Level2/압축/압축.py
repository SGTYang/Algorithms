def solution(msg):
    answer = []
    dic = {}
    for i in range(1,27):
        dic[chr(i+64)] = i
    
    index = 0
    check = 1
    while index<len(msg):
        if index+check == len(msg)+1:
            answer.append(dic.get(msg[index:index+check-1]))
            break
        elif msg[index:index+check] in dic:
            check+=1
        else:
            answer.append(dic.get(msg[index:index+check-1]))
            dic[msg[index:index+check]] = len(dic)+1
            index += check-1
            check =1    
    return answer
