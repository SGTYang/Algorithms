class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        std_len = len(s1)
        counter = Counter(s1)
        
        for i in range(len(s2)-std_len+1):
            com = Counter(s2[i:i+std_len])

            if counter == com:
                return True
        return False
