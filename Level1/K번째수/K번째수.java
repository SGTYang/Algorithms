import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] array, int[][] commands) {
        Queue<Integer> que = new LinkedList<>();
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] answer = {};
        for(int i=0; i<commands.length; i++){
            for(int j=0; j<commands[0].length; j++){
                que.add(commands[i][j]);
            }
        }
        while(!que.isEmpty()){
            int [] tmp = array;
            tmp=Arrays.copyOfRange(tmp, que.poll()-1, que.poll());
            Arrays.sort(tmp);
            list.add(tmp[que.poll()-1]);
        }
        return list;
    }
}
