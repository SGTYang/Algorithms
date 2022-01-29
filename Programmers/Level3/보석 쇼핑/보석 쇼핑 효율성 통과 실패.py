def solution(gems):
    arry = []
    answer = []
    left, pointer =0, 1

    while pointer < len(gems)+1:
        if len(set(gems[left:pointer])) < len(set(gems)):
            pointer += 1
        elif len(set(gems[left:pointer])) == len(set(gems)):
            if len(set(gems[left+1:pointer])) == len(set(gems)):
                left += 1
                arry.append([left,pointer])
            else:
                arry.append([left,pointer])
                left+=1
    
    min_leng = float('inf')
    for i in range(len(arry)):
        if min_leng > len(gems[arry[i][0]:arry[i][1]]):
            answer = [arry[i][0]+1,arry[i][1]]
            min_leng = len(gems[arry[i][0]:arry[i][1]])
    
    return answer
