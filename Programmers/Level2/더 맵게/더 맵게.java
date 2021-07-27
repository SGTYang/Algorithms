import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> que = new PriorityQueue<>();

        for(int i=0; i<scoville.length; i++){
            que.add(scoville[i]);
        }
        while(!check(que, K)){
            int tmp =que.poll();
            que.add(tmp+que.poll()*2);
            answer++;
            if(que.peek() < K && que.size()==1){
                return -1;
            }
        }
        return answer;
    }
    boolean check(PriorityQueue que, int K){
        if((int)que.peek() >= K){
            return true;
        }
        return false;
    }
    
}
