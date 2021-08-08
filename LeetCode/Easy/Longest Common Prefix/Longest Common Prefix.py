class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        answer = ""
        for i in range(0,len(strs[0])):
            com = strs[0][:i+1]
            for j in range(1,len(strs)):
                if not strs[j].startswith(com):
                    return answer
            answer = com
        return answer
