class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String a = phone_number.substring(phone_number.length()-4, phone_number.length());
        String b = "";
        for(int i=0; i<phone_number.length()-4; i++){
            b+="*";
        }
        answer = b+a;
        return answer;
    }
}
