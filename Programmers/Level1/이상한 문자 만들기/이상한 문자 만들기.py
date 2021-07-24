def solution(s):
    index = 0
    s = list(s)
    
    for i in range(len(s)):
        if s[i] == " ":
            index = 0
            continue
        if index % 2 == 0:
            s[i] = s[i].upper()
            index += 1
        elif index % 2 == 1:
            s[i] = s[i].lower()
            index += 1
            
    return "".join(s)
