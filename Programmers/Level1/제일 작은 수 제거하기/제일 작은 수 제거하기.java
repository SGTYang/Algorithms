class Solution {
    public int[] solution(int[] arr) {
        
        if(arr.length<=1){
            int[] answer = new int[]{-1};
            return answer;
        } 
            
            int[] answer = new int[arr.length-1];
            
            int cnt=0;
            int val = arr[0];
        
         for(int i=1; i<arr.length; i++){
             if(val>arr[i]){
                  cnt = i;
                  val = arr[i];
             }
         }
        if(cnt==0){
            for(int i=0; i<arr.length-1; i++){
                answer[i] = arr[i+1];
            }
        }else if(cnt==arr.length-1){
            for(int i=0; i<arr.length-1; i++){
                 answer[i] = arr[i];
            }
        }else{
            for(int i=0; i<cnt; i++){
                answer[i] = arr[i];
            }
            for(int i=cnt; i<arr.length-1; i++){
                answer[i] = arr[i+1];
            }
            }
        return answer;
        }
}
