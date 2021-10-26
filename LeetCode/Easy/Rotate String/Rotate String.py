class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        for i in range(len(s)-1):
            tmp = s[1:]
            tmp.append(s[0])
            s = tmp

            if "".join(s) == goal:
                return True
        return False
        
