class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        new_arry = nums1+nums2
        
        new_arry.sort()
        
        if len(new_arry)%2 != 0:
            index = len(new_arry)//2
            return new_arry[index]
        else:
            index = len(new_arry)//2
            return (new_arry[index-1]+new_arry[index])/2 
