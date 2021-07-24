import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int a=0;
        while(true){
            a = n%10;
            answer+=a;
            n=n/10;
            if(n==0){
                break;
            }
        }
        return answer;
    }
}
