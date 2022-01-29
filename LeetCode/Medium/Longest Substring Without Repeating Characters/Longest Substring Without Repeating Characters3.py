class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        max_len = 0
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]]+1
            else:
                max_len = max(max_len, i-start+1)
            
            dic[s[i]] = i
            
        return max_len
