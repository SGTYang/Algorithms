class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int a=0;
        int tmp=0;
        int sum=0;
        
        for(int i=0; i<d.length-1; i++){
            tmp=i;
            for(int j=i+1; j<d.length; j++){
                if(d[tmp]>d[j]){
                    tmp=j;
                }
            }
            a = d[tmp];
            d[tmp]=d[i];
            d[i]=a;
        }
        
        for(int i=0; i<d.length; i++){
            if(sum+d[i]<=budget){
                sum+=d[i];
                answer++;
            }
        }
         return answer;
    }
}
