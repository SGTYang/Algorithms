import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int index = 0;
        boolean[] visit = new boolean[n+1];
        Queue<Integer> que = new LinkedList<Integer>();
        
        while(index<n){
            if(!visit[index]){
                answer++;
                que.add(index);
                visit[index]=true;
            
                while(!que.isEmpty()){
                    int q = que.poll();
                    for(int j=0; j<computers[q].length; j++){
                        if(q!=j && computers[q][j]==1){
                            if(!visit[j]){
                                que.add(j);
                                visit[j]=true;
                                }
                            }
                        }
                    }
            }
            index++;
        }
        return answer;
    }
}
