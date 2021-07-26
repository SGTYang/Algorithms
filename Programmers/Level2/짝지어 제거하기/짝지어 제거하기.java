import java.util.*;
class Solution
{
    public int solution(String s){
        int answer=0;
        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<s.length(); i++){
            if(!stack.empty() && stack.peek()==(int)s.charAt(i)){
                stack.pop();
            }else{
                stack.push((int)s.charAt(i));
            }
            
        }

        if(stack.empty()){
            answer=1;
        }
        return answer;
    }
}
