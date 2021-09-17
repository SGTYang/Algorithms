class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split(" ")
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        return " ".join(s_list)
