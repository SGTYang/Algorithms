class Solution:
    def intToRoman(self, num: int) -> str:
        num_arry = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rom = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        answer = ''
        def conv(num, index, answer):
            answer += (num//num_arry[index])*rom[index]
            num = num%num_arry[index]
            if index == 0:
                return answer
            return conv(num, index-1, answer)    
        return (conv(num, len(num_arry)-1, answer))
