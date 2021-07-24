import java.util.*;
class Solution {
    public int[] solution(long n) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] answer = {};
        long num =0;
        int numI =0;
        while(n!=0){  
            num = n%10;
            numI = (int)num;
            list.add(numI);
            n/=10;
        }
        
        answer = new int[list.size()];
        
        for(int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}
