class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        subset = ""
        index = 0
        result = []
        def backtrack(subset, index):
            print(subset)
            
            if len(subset) == len(s):
                result.append(subset)
            else:
                if s[index].isalpha():
                    backtrack(subset+s[index].swapcase(), index + 1)
                backtrack(subset + s[index], index + 1)

        backtrack(subset, index)
        return result
                            
