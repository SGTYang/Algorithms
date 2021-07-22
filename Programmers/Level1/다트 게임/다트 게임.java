class Solution {
    public int solution(String dartResult) {
        
        int answer = 0;
        int num = 0;
        int cnt =0;
        int [] sum = new int [3]; // 문자열 3세트를 배열로 받아주기위해
        
        for(int i=0; i<dartResult.length(); i++){
            // 문자열이 3세트면 break
            if(cnt>2){
                break;
            }
            
            // 문자열에 숫자있는지 확인해준다
            for(int k=0; k<11; k++){
                // 10을 확인해주기 위해서 i번째 위치 숫자와 i+1번째 위치 숫자를 확인해준다
                if(dartResult.charAt(i)-'0'==1 && dartResult.charAt(i+1)-'0'==0) {
                    num=10;
                    // 10이 있으면 i+1번째 숫자를 건너뛰기 위해 i에 1을 더해준다
                    i++;
                    //숫자면 다음 문자열로 넘어가기위해 continue 사용
                    continue;
                }
                // 10이 아닐때 0~9사이 숫자확인
                if(dartResult.charAt(i)-'0'==k){
                    num=k;
                    continue;
                }
            }
            
            // 비교해서 S면 num^1 해준 값을 sum[문자열셋트]에 넣어준다
            if(dartResult.charAt(i)=='S'){
                sum[cnt]+=num*1;
                // 아래의 코드 실행하기위해 i의 범위를 확인해준다
                if(i<dartResult.length()-1){
                    // 다음 문자열(i+1)자리에 #이나 *가 있는지 확인(#,*는 하나만 존재 가능)
                    if(dartResult.charAt(i+1)!='#' && dartResult.charAt(i+1)!='*' ){
                        // #, *는 항상 문자열셋 마지막에 존재 그래서 다음 문자열로 이동 시켜주기위해 cnt++
                        cnt++;
                    }
                }
                // 다음 문자열로 넘어가기위해 
                continue;
            }else if(dartResult.charAt(i)=='D'){
                sum[cnt]+=num*num;
                 if(i<dartResult.length()-1){
                    if(dartResult.charAt(i+1)!='#' && dartResult.charAt(i+1)!='*' ){
                        cnt++;
                    }
                }
                continue;
            }else if(dartResult.charAt(i)=='T'){
                sum[cnt]+=num*num*num;
                if(i<dartResult.length()-1){
                    if(dartResult.charAt(i+1)!='#' && dartResult.charAt(i+1)!='*' ){
                        cnt++;
                    }
                }
                continue;
            }
            //*,#는 문자열셋 마지막에 온다 그래서 아래 코드 실행이 끝나면 문자열셋을 옮겨준다(cnt++)해준다
            if(dartResult.charAt(i)=='*'){
                sum[cnt]=sum[cnt]*2;
                // i이전 문자열셋이 있으면 그 문자열셋에도 2를 곱해준다
                if(cnt-1>=0){
                    sum[cnt-1]=sum[cnt-1]*2;
                }
                cnt++;
                continue;
            }else if(dartResult.charAt(i)=='#'){
                sum[cnt]=sum[cnt]*(-1);
                cnt++;
                continue;
            }
        }

        // 문자열셋을 더해준다
        answer = sum[0]+sum[1]+sum[2];
        return answer;
  }
}
