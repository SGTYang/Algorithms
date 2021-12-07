class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1
        
        while left<right:
            
            num_sum = numbers[left] + numbers[right]
            
            if num_sum == target:
                return [left+1, right+1]
            
            elif num_sum > target:
                right -= 1
            
            else:
                left +=1
