class Solution {
    public String solution(String s) {
        String answer = "";
        int mid = s.length()/2;
        if(s.length()%2==0){
            answer = Character.toString(s.charAt(mid-1))+Character.toString(s.charAt(mid));
        }else{
            answer = Character.toString(s.charAt(mid));
        }
        return answer;
    }
}
