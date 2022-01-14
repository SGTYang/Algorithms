def solution(s):
    if len(s) == 1:
        return 1
    words_group_length = len(s)//2
    words_length_arry = []
    
    for i in range(1,words_group_length+1):
        tmp_str = ""
        index = s[:i]
        count = 1
        
        for j in range(i,len(s)-len(s)%i,i):
            if index != s[j:j+i]:
                if count >=2:
                    tmp_str += str(count)+index
                    count = 1
                else:
                    tmp_str += index
                index = s[j:j+i]
            else:
                count += 1
        if count >= 2:
            tmp_str += str(count)+index
        else:
            tmp_str += index
        if len(s)%i  == 0:
            words_length_arry.append(len(tmp_str))
        else:
            words_length_arry.append(len(tmp_str+s[-(len(s)%i):]))

    return min(words_length_arry)
    
    return answer
