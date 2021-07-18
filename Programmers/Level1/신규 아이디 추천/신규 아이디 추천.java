import java.util.*;
class Solution {
    public String solution(String new_id) {
        String answer = "";
        ArrayList<String> list = new ArrayList<String>();
        // 대문자를 소문자로(1단계)
        new_id = new_id.toLowerCase();
        
        // 쓸대 없는것들 제거
        for(int i=0; i<new_id.length(); i++){
            if(!(new_id.charAt(i)<=122 && new_id.charAt(i)>=97)){
                if(!(new_id.charAt(i)<=57 && new_id.charAt(i)>=48)){
                    if(new_id.charAt(i)!='-' && new_id.charAt(i)!='_'){
                        if(new_id.charAt(i)!='.'){
                            if(i==0){
                                new_id = new_id.substring(1,new_id.length());
                                i--;
                            }else if(i==new_id.length()-1){
                                new_id = new_id.substring(0,new_id.length()-1);
                                i--;
                            }else{
                                new_id = new_id.substring(0,i)+new_id.substring(i+1,new_id.length());
                                i--;
                            }
                        }
                    }
                }
            }
        }
        
        // . 연속되면 1개 제거
        for(int i=0; i<new_id.length()-1; i++){
            if(new_id.charAt(i)=='.' && new_id.charAt(i+1)=='.'){
                if(i==0){
                    new_id = new_id.substring(1,new_id.length());
                    i--;
                }else if(i==new_id.length()-2){
                    new_id = new_id.substring(0,new_id.length()-2);
                    i--;
                }else{
                    new_id = new_id.substring(0,i)+new_id.substring(i+1,new_id.length());
                    i--;
                }
            }
        }
        
        // 마지막이나 처음에 . 있으면 제거
        if(new_id.length()<2 && new_id.charAt(0)=='.'){
            new_id = "";
        }else{
            if(new_id.charAt(0)=='.'){
                new_id = new_id.substring(1,new_id.length());
            }
            if(new_id.charAt(new_id.length()-1)=='.'){
                new_id = new_id.substring(0,new_id.length()-1);
            }
        }
        
        System.out.println(new_id);

        // 빈 문자열이면 a 대입
        if(new_id.length()==0){
            new_id = "a";
        }
        // 16자 이상이면 15개 문자를 제외한 나머지 제거
        if(new_id.length()>15){
            for(int i=0; i<16; i++){
                list.add((Character.toString(new_id.charAt(i))));  
            }
            new_id="";
            for(int i=0; i<15; i++){
                new_id+=list.get(i);  
            }
        }
        
        // 마지막에 .있으면 제거
        if(new_id.charAt(new_id.length()-1)=='.'){
            new_id = new_id.substring(0,new_id.length()-1);
        }
        
        if(new_id.length()<=2){
            for(int i=new_id.length(); i<3; i++){
                new_id+=Character.toString(new_id.charAt(new_id.length()-1));
            }
        }
      
        answer = new_id;
        return answer;
    }
        
}
