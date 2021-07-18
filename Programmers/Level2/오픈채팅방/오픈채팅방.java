import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        String[][] list = new String[record.length][3];
        HashMap<String, String> map = new HashMap();
        StringBuilder compressed = new StringBuilder();
        ArrayList<String> arr = new ArrayList<String>();

        for(int i=0; i<record.length; i++){
            String [] tmp = record[i].split(" ");
            list[i]=tmp;
        }
        for(int i=0; i<record.length; i++){
            if(!map.containsKey(list[i][1])){
                map.put(list[i][1],list[i][2]);
            }
            
            if(list[i][0].equals("Change") || list[i][0].equals("Enter")){
                map.put(list[i][1], list[i][2]);
            }
        }

        for(int i=0; i<record.length; i++){
            if(list[i][0].equals("Change")){
                continue;
            }
            compressed.setLength(0);
            compressed.append("");
            compressed.append(map.get(list[i][1]));
            if(list[i][0].equals("Enter")){
                compressed.append("님이 들어왔습니다.");
            }
            if(list[i][0].equals("Leave")){
                compressed.append("님이 나갔습니다.");
            }
            arr.add(compressed.toString());
        }
        
        String[] answer = new String[arr.size()];
        for(int i=0; i<arr.size(); i++){
            answer[i]=arr.get(i);
        }
        return answer;
    }
}
