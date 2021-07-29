import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        ArrayList<Integer> ans = new ArrayList<Integer>();
        int[] answer;
        int t=0;
        int a=0;
        int cnt=1;
        
        //progresses 길이 만큼 while 동작
        while(a<progresses.length){
            // 반복문 시작할 때 마다 t가 1씩 증가
            t++;
            // 진도가100%이거나 100%를 넘어야 작업이 완료 
            // 즉 progresses + speed*시간(t) 값이 100이거나 100을 넘어야 한다
            if(100-progresses[a] <= speeds[a]*t){
                // 빈 어레이 리스트에 t값을 넣어준다
                list.add(t);
                // a를 1증가 시켜 인덱스를 이동시켜준다
                a++;
                // t값 초기화
                t=0;
            }
        }
        //어레이 리스트 안에 프로그레스를 완료하기 까지 걸린 시간이 저장되어 있다 {7,3,9}...
        // 앞에 작업이 끝나기 전에는 뒤에 있는 작업이 끝나지 않는다 
        
        // 즉 앞t값이 뒤t값보다 크거나 같으면 앞의 작업이 끝날때 같이 배포
        
        // 비교할 초기값 설정
        int tmp = list.get(0);
        for(int i=1; i<list.size(); i++){
            // 초기값과 불러온 값 비교
            if(tmp>= list.get(i)){
                cnt++;
                continue;
            }else{
                //뒤의 작업이 클때
                //이때 까지의 cnt를 저장하고 1로 초기화 해주고 뒤 작업의 값을 비교할 초기값으로 설정
                ans.add(cnt);
                tmp=list.get(i);
                cnt=1;
            } 
        }
        // 마지막 남은 t값 넣어주기 
       ans.add(cnt);
        
        //어레이 리스트를 배열로 넣어주기
        answer = new int[ans.size()];
        for(int i=0; i<ans.size(); i++){
            answer[i]=ans.get(i);
        }
        return answer;
    }
}
