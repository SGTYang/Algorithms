class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        
        for i in nums1:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        
        answer = []
        
        for i in nums2:
            if i in dic and dic[i] >0:
                dic[i] -= 1
                answer.append(i)
                
        return answer
