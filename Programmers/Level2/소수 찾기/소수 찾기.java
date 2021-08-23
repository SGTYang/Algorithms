import java.util.*;
public class Solution {
    public static HashSet<Integer> prime = new HashSet<>();
    public static int cnt = 0;
    public static boolean[] NUMBER = new boolean[10000000];
    public static int solution(String input){
    	// StringBuilder를 통해 숫자를 만든다.
        StringBuilder sb = new StringBuilder();
        Arrays.fill(NUMBER, true);
        NUMBER[0] = NUMBER[1] = false;

        String[] numbers = input.split("");
        boolean[] picked = new boolean[numbers.length];
        makeNumber(numbers, picked, sb);

        for(int num : prime){
            if(isPrime(num))
                cnt++;
        }
        return cnt;
    }
    public static void makeNumber(String[] numbers, boolean[] picked, StringBuilder sb){
        // numbers : 숫자 후보
        // picked : 선택되었는 가를 보여주는 예시
        // 기저 사례: picked가 모두 true면 return
        int len = picked.length;
        boolean finished = true;
        for(boolean flag : picked){
            if(!flag){
                finished = false;
                break;
            }

        }
        if(finished) return;

        for(int i = 0; i < len; i++){
            if(!picked[i]){
                sb.append(numbers[i]);
                prime.add(Integer.parseInt(sb.toString()));
                picked[i] = true;
                makeNumber(numbers, picked, sb);
                picked[i] = false;
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }

    public static boolean isPrime(int num){
    	// 에라토스테네스의 체를 이용
        for(int i = 2; i <= Math.sqrt(num); i++){
            for(int j = 2; j * i <= num ; j++){
                NUMBER[j * i] = false;
            }
        }
        return NUMBER[num];
    }

}
