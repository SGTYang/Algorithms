import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer ="";
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(String i : participant){
            if(map.containsKey(i)){
            map.put(i, map.get(i)+1);
        }else{
            map.put(i, 1);
            }
        }

        for(String i : completion){
            map.put(i, map.get(i)-1);
        }

        for(String i : participant){
            if(map.get(i)!=0){
                answer=i;
                break;
            }
        }
            return answer;
    }
}
