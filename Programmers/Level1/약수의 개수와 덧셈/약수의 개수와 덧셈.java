class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i=left; i<=right; i++){
            int cnt = 0;
            int tmp = 0;
            System.out.println(i);
            for(int j=1; j<=i/2; j++){
                if(i%j == 0){
                    cnt++;
                }
            }
 
            if((cnt+1)%2!=0){
                tmp = i*(-1);
            }else{
                tmp = i;
            }
            
            answer += tmp;
        }
        return answer;
    }
}
