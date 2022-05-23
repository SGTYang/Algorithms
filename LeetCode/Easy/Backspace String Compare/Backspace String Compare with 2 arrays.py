class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        tmp_s, tmp_t = [], []
        
        for i in range(len(s)):
            if s[i] == '#':
                tmp_s = tmp_s[:-1]
            else:
                tmp_s.append(s[i])
        
        for i in range(len(t)):
            if t[i] == '#':
                tmp_t = tmp_t[:-1]
            else:
                tmp_t.append(t[i])
            
        if tmp_s == tmp_t:
            return True
        return False
