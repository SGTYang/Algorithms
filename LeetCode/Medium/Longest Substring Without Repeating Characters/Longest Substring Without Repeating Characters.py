class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dic = []
        max_len = 0
        
        for i in range(len(s)):
            
            if s[i] in str_dic:
                str_dic = str_dic[str_dic.index(s[i])+1:len(str_dic)]
                str_dic.append(s[i])
            else:
                str_dic.append(s[i])
                max_len = max(len(str_dic), max_len)

        return max_len
