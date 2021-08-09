class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = list(counter.keys())
        
        ans = set()
        
        if counter[0] >= 3: 
            ans.add((0, 0, 0))
            
        pos, neg = [x for x in nums if x > 0], [x for x in nums if x < 0]
        
        for a in neg:
            for b in pos:
                c = -(a + b)
                if c in counter and ((c != a and c != b) or counter[c] > 1):
                    ans.add(tuple(sorted([a, b, c])))
        return ans
