class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend/divisor>2**31-1:
            return 2**31-1
        elif dividend/divisor<-2**31:
            return -2**31
        else:
            return int(dividend/divisor)
