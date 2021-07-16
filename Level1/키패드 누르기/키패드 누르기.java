import java.util.*;
class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        int[][] ph_nums = {{1,3},{0,0},{1,0},{2,0},{0,1},{1,1},{2,1},{0,2},{1,2},{2,2}};
        int[] curr_left = {0,3};
        int[] curr_right = {2,3};
        
        for(int i=0; i<numbers.length; i++){
            if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
                curr_left = ph_nums[numbers[i]];
                answer += "L";
            }else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
                curr_right = ph_nums[numbers[i]];
                answer += "R";
            }else{
                int ch_left = Math.abs(curr_left[0]-ph_nums[numbers[i]][0])+Math.abs(curr_left[1]-ph_nums[numbers[i]][1]);
                int ch_right = Math.abs(curr_right[0]-ph_nums[numbers[i]][0])+Math.abs(curr_right[1]-ph_nums[numbers[i]][1]);
                
                if(ch_left == ch_right && hand.equals("right")){
                    curr_right = ph_nums[numbers[i]];
                    answer += "R";
                }else if(ch_left == ch_right && hand.equals("left")){
                    curr_left = ph_nums[numbers[i]];
                    answer += "L";
                }else if(ch_left > ch_right){
                    curr_right = ph_nums[numbers[i]];
                    answer += "R";
                }else if(ch_left < ch_right){
                    answer += "L";
                    curr_left = ph_nums[numbers[i]];
                }
            }
        }
        return answer;
    }
}
