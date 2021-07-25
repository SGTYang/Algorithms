class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        int sum=0;
        int tmp=0;
        
        tmp=x;
        while(tmp!=0){
            sum+=tmp%10;
            tmp=tmp/10;
        }
        if(x%sum==0){
            answer = true;
        }
        return answer;
    }
}
