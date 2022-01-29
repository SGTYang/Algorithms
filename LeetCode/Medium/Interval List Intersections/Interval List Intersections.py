class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first_len = len(firstList)
        second_len = len(secondList)
        i = 0
        j = 0
        result = []
        while i < first_len and j < second_len:
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            
            if first_start <= second_end and second_start <= first_end:
                result.append([max(first_start, second_start), min(first_end, second_end)])
                
            if first_end <= second_end:        
                i += 1              
            else:
                j += 1
                
        return result
