class Solution {
    public String solution(String[] seoul) {
        String answer="";
        String a="김서방은 ";
        String b="에 있다";
        for(int i=0; i<seoul.length; i++){
            if(seoul[i].equals("Kim")){
               answer= a + Integer.toString(i) + b;
                break;
            }
        }
        return answer;
    }
}
