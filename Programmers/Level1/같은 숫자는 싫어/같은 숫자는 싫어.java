import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        int b=10;
        
        for(int i=0; i<arr.length; i++){
            if(arr[i]!=b){
                list.add(arr[i]);
            }
            b=arr[i];
        }
        int [] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++){ 
            answer[i] = list.get(i);
        }
        return answer;
    } 
}
