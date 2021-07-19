class Solution(object):
    def reverse(self, x):
        multiplier = 1
        ans = 0
        
        for i in str(x):
            if i.isalnum():
                ans += int(i) * multiplier
                multiplier *= 10
                
        if ans > pow(2, 31):
            return 0
        elif(x < 0):
            return ans * -1
        return ans
