# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 0 ,n
        
        while left < right:
            index = (left+right)//2
            if isBadVersion(index):
                right = index
            else:
                left = index+1
        return right
