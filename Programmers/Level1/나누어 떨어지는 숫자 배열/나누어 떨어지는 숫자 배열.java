import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
    
        ArrayList<Integer> num = new ArrayList<Integer>();
        
        int[] answer = {};
        int tmp=0;
        // 정렬
        for(int i=0; i<arr.length-1; i++){
            for(int j=i; j<arr.length; j++){
                if(arr[i]>arr[j]){
                    tmp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=tmp;
                }
            }
        }
        
        //나누어 떨어지는지 확인
        for(int i=0; i<arr.length; i++){
            if(arr[i]%divisor==0){
                num.add(arr[i]);
            }
        }
        
        // 나누어 떨어지는 값이 없다면 -1을 넣어준다 이떄 num.size는 0
        if(num.size()==0){
            answer = new int[1];
            answer[0] = -1;
        }

        // 나누어 떨어지는 값이 1개라도 있다면 num.size는 1이상
        // 어레이리스트 num 값을 answer배열에 넣어준다
        else{
            answer = new int[num.size()];
            for(int i=0; i<num.size(); i++){
            answer[i]=num.get(i);
            }
        }
        return answer;
    }
}
