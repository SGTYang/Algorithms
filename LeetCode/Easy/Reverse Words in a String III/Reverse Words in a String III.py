class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")
        
        for i in range(len(s_)):
            s[i] = s_[i][::-1]
        return " ".join(s)
