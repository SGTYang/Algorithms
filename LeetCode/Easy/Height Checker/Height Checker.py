class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expec = sorted(heights)

        cnt = 0
        for i in range(len(heights)):
            if heights[i] != expec[i]:
                cnt += 1
        return cnt
