class Solution:
    def myAtoi(self, s: str) -> int:
        tmp = ''
        negative = False
        check = False
        b = False
        # 48 ~ 57
        for i in range(len(s)):
            if s[i] = ' ':
                continue
            elif s[i] == '-':
                negative = True
                check = True
            elif s[i] == '+':
                check = True
            elif ord(s[i]) >= 47 and ord(s[i]) <= 57:
                tmp += s[i]
            else:
                break
        
        if len(tmp) == 0:
            return 0
        if negative:
            return min(int(tmp), 2**31)*-1
        
        return min(int(tmp), 2**31)
            
        
