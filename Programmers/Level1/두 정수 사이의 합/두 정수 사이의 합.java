class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
    if(a>b){
        int c=a;
        a=b;
        b=c;
    }
    for(int i=a; i<=b; i++){
        answer=answer+i;
        }
    return answer;
    }
}
