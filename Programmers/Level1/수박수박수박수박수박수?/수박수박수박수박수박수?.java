class Solution {
    public String solution(int n) {
        String a = "수";
        String answer = "";
        int quo = n/2;
        
        if(n==1){
            answer="수";
            return answer;
        }
        for(int i=0; i<quo; i++) {
            String result = new String(new char[i]).replace("\0", "수박");
            answer="수박"+result;
            if(n%2!=0){
              answer=answer+"수";
            }
        }
            return answer;
        }
    }
