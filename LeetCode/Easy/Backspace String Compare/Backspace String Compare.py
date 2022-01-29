class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        dic_s = {}
        dic_t = {}
        start = 0
        
        for i in range(len(s)):
            if s[i] == '#' and len(dic_s)!=0:
                del dic_s[start-1]
                start -= 1
            else:
                if s[i] != '#':
                    dic_s[start] = s[i]
                    start += 1
                
        start = 0
        for i in range(len(t)):
            if t[i] == '#' and len(dic_t)!=0:
                del dic_t[start-1]
                start -= 1
            else:
                if t[i] != '#':
                    dic_t[start] = t[i]
                    start += 1
                
        print(dic_s, dic_t)
        ss = ''
        tt = ''
        for i in range(len(dic_s)):
            ss += dic_s[i]
        for i in range(len(dic_t)):
            tt += dic_t[i] 
                
        if ss == tt:
            return True
        else:
            return False
