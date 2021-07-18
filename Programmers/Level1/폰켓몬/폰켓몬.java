import java.util.*;
class Solution {
    public int solution(int[] nums) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int answer = 0;
        int n=nums.length/2;
        // 중복제거
        for(int i=0; i<nums.length; i++){
            if(!list.contains(nums[i])){
                list.add(nums[i]);
            }
        }
        
        for(int i=0; i<list.size(); i++){
            System.out.println(list.get(i));
        }
        
        if(n>list.size()){
            answer=list.size();
        }else{
            answer=n;
        }
        return answer;
    }
}
