class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) != ' '){
                if(65 <= (int)s.charAt(i) && (int)s.charAt(i) <= 90){
                    if((int)s.charAt(i)+n > 90){
                        answer += Character.toString((char)((int)s.charAt(i)+n-26));
                    }else{
                        answer += Character.toString((char)((int)s.charAt(i)+n));
                    }
                }else if(97 <= (int)s.charAt(i) && (int)s.charAt(i) <= 122){
                    if((int)s.charAt(i)+n > 122){
                        answer += Character.toString((char)((int)s.charAt(i)+n-26));
                    }else{
                        answer += Character.toString((char)((int)s.charAt(i)+n));
                    }
                }
            }else{
                answer += " ";
            }
        }
        return answer;
    }
}
