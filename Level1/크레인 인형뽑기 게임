import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for(int i=0; i<moves.length; i++){
            int a=moves[i]-1;      
            for(int j=0; j<board.length; j++){
                if(board[j][a]!=0){
                    list.add(board[j][a]);
                    board[j][a]=0;
                    break;
                }   
            }
        }
        if(list.size()==0 || list.size()==1){
            return answer;
        }
        for(int i=0; i<list.size()-1; i++){
            if(list.get(i)==list.get(i+1)){
                list.remove(i+1);
                list.remove(i);
                i = -1;
                answer+=2;
            }
        }
        return answer;  
    }
}
