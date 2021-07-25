class Solution {
    public long solution(long n) {
        long answer = -1;
        long sum =1;
        if(n==1){
            answer=4;
        }
        for(int i=1; i<n; i++){
            if(n==i*i){
                answer= (i+1)*(i+1);
                break;
            }
        }
        return answer;
    }
}
