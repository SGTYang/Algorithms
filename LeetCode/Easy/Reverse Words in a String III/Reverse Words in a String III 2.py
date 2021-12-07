class Solution:
    def reverseWords(self, s: str) -> str:
        
        list_s = s.split(" ")
        
        for i in range(len(list_s)):
            
            left, right = 0, len(list_s[i])-1
            tmp = list(list_s[i])
            while left<=right:
                
                tmp[left], tmp[right] = tmp[right], tmp[left]
                
                left+=1
                right-=1
                
            list_s[i] = "".join(tmp)
            
        return " ".join(list_s)
