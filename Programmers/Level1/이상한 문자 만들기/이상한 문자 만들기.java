class Solution {
    public String solution(String s) {
        String answer = "";
        String a = "";
        int num =0;
        int c = 0;
        int d  = 0;
        for(int i=0; i<s.length(); i++){
           
            // s.charAt(i): 문자열에서 i번째 값을 char형으로 반환
            // Character.toString char를 string으로 변환
            // 공백이 나왔을때 or 인덱스 끝일때
            if(Character.toString(s.charAt(i)).equals(" ") || i==s.length()-1){
                
                // 그때의 i값을 num에 저장
                num=i;
                
                // c: 공백이 나오기전의 인덱스값(초기값:0) 
                // c~num 범위(공백이 나오기전 인덱스값 부터 공백이 나온 인덱스 까지)
                for(int j=c; j<=num; j++){
                    
                    //d: 1씩 증가하는 정수, 이 문자가 홀수번째로 왔는지 짝수번째로 왔는지 판별
                    if(d%2==0){
                        a = Character.toString(s.charAt(j));
                        a=a.toUpperCase();
                        d++;
                    }else{
                        a = Character.toString(s.charAt(j));
                        a=a.toLowerCase();
                        d++;
                    }
                    // 결과값들 합치기
                    answer = answer+a;
                }
                // 값들 초기화 
                d=0;
                //num이 공백까지의 인덱스니까 그 다음 인덱스로 선언2
                c=num+1;
            }
            
        }
        return answer;
    }
}
