class Solution{
    public int solution(int n, int a, int b){
        int answer = 1;
        
        if(a>b){
            int tmp=a;
            a=b;
            b=tmp;
        }
        
        while(true){ 
            if(b-a==1 && b % 2 == 0){
                break;
            }
            if(a%2!=0){
            a=a+1;
            }
            if(b%2!=0){
            b=b+1;
            }
            a=a/2;
            b=b/2;
            answer++;
        }
        
        return answer;
    }
}
