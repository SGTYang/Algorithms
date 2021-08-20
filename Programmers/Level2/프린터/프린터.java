import java.util.*;
class Solution {
   public int solution(int[] priorities, int location) {
        int answer = 1;

        PriorityQueue priority = new PriorityQueue<>(Collections.reverseOrder());

        for(int task : priorities){
            priority.add(task);
            //System.out.println(priority);
        }
        //{2,5,4,1,3};

        System.out.println(priority);
        while(!priority.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if(priorities[i] == (int)priority.peek()) {
                    if(i == location){
                        return answer;
                    }
                    priority.poll();
                    answer++;
                }
            }
        }

        return answer;
    }
}
