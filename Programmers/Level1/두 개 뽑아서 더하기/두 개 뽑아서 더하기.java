import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> sum = new ArrayList<>();
        
        for(int i=0; i<numbers.length; i++){
            for(int j=i+1; j<numbers.length; j++){
                sum.add(numbers[i]+numbers[j]);
            }
        }

        for(int i=0; i<sum.size(); i++){
            if(!list.contains(sum.get(i))){
                list.add(sum.get(i));
            }
        }
        Collections.sort(list);
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++) {
        	answer[i] = list.get(i);
        }
        return answer;
    }
}
