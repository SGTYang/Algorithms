import java.util.Arrays;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        
        char[] result = new char[strings.length];
        char first = 0;
        
        //배열안의 n의 자리 수를 char[] result 에 넣어줌
        for(int i = 0 ; i < strings.length ; i++){
            first = strings[i].charAt(n);
            result[i] = first;
        }
        
        //result에 넣어준 값과 원래 값을 더해줘서 answer 로 합쳐줌
        for(int i = 0 ; i < strings.length ; i++){
            answer[i] = strings[i];
            answer[i] = result[i] + answer[i];
        }
        // 정렬
        Arrays.sort(answer);
        
        for(int i = 0 ; i < result.length ; i++){
            answer[i] = answer[i].substring(1);
        }
        
        return answer;
    }
}
