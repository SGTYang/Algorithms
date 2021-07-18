import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int [] a = {1,2,3,4,5};
        int [] b = {2,1,2,3,2,4,2,5};
        int [] c = {3,3,1,1,2,2,4,4,5,5};
        ArrayList<Integer> list = new ArrayList<Integer>();
        int aCount=0, bCount=0, cCount=0;
        
        for(int i=0; i<answers.length; i++){
            if(a[i%a.length]==answers[i]){
                aCount++;
            }
            if(b[i%b.length]==answers[i]){
                bCount++;
            }
            if(c[i%c.length]==answers[i]){
                cCount++;
            }
        }
        int max = Math.max(aCount,Math.max(bCount,cCount));
        if(max==aCount){
            list.add(1);
        }
        if(max==bCount){
            list.add(2);
        }
        if(max==cCount){
            list.add(3);
        }
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            answer[i]=list.get(i);
        }
        return answer;
    }
}
