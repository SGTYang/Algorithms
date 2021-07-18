def solution(participant, completion):

    dic = {}
    
    for i in range(0, len(participant)):
        if dic.get(participant[i]) != None:
            dic[participant[i]] = dic.get(participant[i])+1
        else:
            dic[participant[i]] = 1
    
    for i in range(0, len(completion)):
        dic[completion[i]] = dic.get(completion[i])-1
            
    for i in dic:
        if dic.get(i) !=0:
            answer = i

    return answer
