class Solution {
    public String solution(int a, int b) {
        String[] day ={"SUN","MON","TUE","WED","THU","FRI","SAT"};
        String answer = "";

        switch(a){
        case 1:
            answer=day[(b%7+4)%7];
            break;
        case 2:
            answer=day[(b%7+0)%7];
            break;
        case 3:
            answer=day[(b%7+1)%7];
            break;
        case 4:
            answer=day[(b%7+4)%7];
            break;
        case 5:
            answer=day[(b%7-1)%7];
            break;
        case 6:
            answer=day[(b%7+2)%7];
            break;
        case 7:
            answer=day[(b%7+4)%7];
            break;
        case 8:
            answer=day[(b%7+0)%7];
            break;
        case 9: 
            answer=day[(b%7+3)%7];
            break;
        case 10:
            answer=day[(b%7+5)%7];
            break;
        case 11:
            answer=day[(b%7+1)%7];
            break;
        case 12:
            answer=day[(b%7+3)%7];
            break;
        default:
            break;
        }
        return answer;       
    }
}
