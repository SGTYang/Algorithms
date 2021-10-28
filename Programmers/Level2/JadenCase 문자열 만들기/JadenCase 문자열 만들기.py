def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        if len(s[i]) > 0:
            s[i] = s[i].lower()
            s[i]  = list(s[i])
            if s[i][0].isalpha():
                s[i][0] = s[i][0].upper()
            s[i] = "".join(s[i])
    return " ".join(s)
