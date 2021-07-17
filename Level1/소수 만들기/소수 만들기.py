import Math
def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                print(nums[i]+nums[j]+nums[k])

    return answer

def prime(number):
    if(number == 0 or number == 1):
        return false
    
    for i in range(2,Math.sqrt(number)):
        if(number%i==0)
'''boolean prime(int n){
        if(n==0 || n==1){
        
        
            return false;
        }
        for(int i=2; i<=(int)Math.sqrt(n); i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }'''
