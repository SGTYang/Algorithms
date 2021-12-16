class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr)<3:
            return False
        val = arr[0]
        decrease = False
        increase = False
        for i in range(1,len(arr)):
            if decrease:
                if val<=arr[i]:
                    return False
            else:
                if val>arr[i]:
                    decrease = True
                elif val == arr[i]:
                    return False
                else:
                    increase = True
            val = arr[i]
            
        if decrease and increase:
            return True
        else:
            return False
