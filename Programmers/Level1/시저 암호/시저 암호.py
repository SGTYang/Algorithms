def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        if s[i].islower():
            answer += chr((ord(s[i])+n-ord('a'))%26+ord('a'))
        elif s[i].isupper():
            answer += chr((ord(s[i])+n-ord('A'))%26+ord('A'))
        else:
            answer += " "
    return answer
