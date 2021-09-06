class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            if arr[i]*2 in arr:
                if arr.index(arr[i]*2) != i:
                    return True
        return False
