def solution(s):
    num_list = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    answer = 0
    arry = []
    tmp = ''
    for i in range(len(s)):
        if ord(s[i]) >= 58 or ord(s[i]) <= 47:
            tmp += s[i]
            if num_list.get(tmp) is not None:
                arry.append(num_list[tmp])
                tmp = ''
        else:
            arry.append(str(s[i]))

    answer = int("".join(arry))
    return answer
