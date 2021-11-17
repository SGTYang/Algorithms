def solution(s):
    open_parentheses = ['[','(','{']
    close_parentheses = [']',')','}']
    s = list(s)
    answer = 0
    i = 0
    
    def parentheses_check(s):
        stack = []
        for i in range(len(s)):
            if s[i] in open_parentheses:
                stack.append(close_parentheses[open_parentheses.index(s[i])])
            else:
                if len(stack) !=0 and stack[-1] == s[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
    
    while i < len(s):
        if parentheses_check(s):
            answer += 1
        s = list("".join(s[1:])+"".join(s[0]))
        i += 1

    return answer
