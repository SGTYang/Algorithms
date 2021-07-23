class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        
        char check;
        
        int n = s.length();
        if(n==4 || n==6){

         if(s.equals(""))
        {
            //문자열이 공백인지 확인
            return false;
        }

       for(int i = 0; i<s.length(); i++){
            check = s.charAt(i);
           
            if( check < 48 || check > 58)
            {
                //해당 char값이 숫자가 아닐 경우
                return false;
            }
       }
        return answer;
        }else{
        return false;
        }
    }
}
