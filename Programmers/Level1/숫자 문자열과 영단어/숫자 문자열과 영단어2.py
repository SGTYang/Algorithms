def solution(s):
    answer = ''
    
    word_dict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    start = 0
    pointer = 1
    
    while pointer < len(s)+1:

        if s[start:pointer] in word_dict:
            answer+= word_dict[s[start:pointer]]
            start = pointer
            pointer += 1
        
        elif s[start:pointer].isdigit():
            answer += s[start:pointer]
            start = pointer
            pointer += 1
        else:
            pointer += 1
    
    return int(answer)
