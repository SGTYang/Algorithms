class Solution {
    public String solution(String p) {
        return vLoop(p);
    }
    
    String vLoop(String p){
        if(p.length()==0){
            return p;
        }
        StringBuilder u = new StringBuilder();
        StringBuilder v = new StringBuilder();
        StringBuilder tmp = new StringBuilder();
        u.append(p.substring(0,split(p)));
        v.append(p.substring(split(p), p.length()));
        if(check(u.toString())){
            return u.append(vLoop(v.toString())).toString();
        }else{
            tmp.append("(");
            tmp.append(vLoop(v.toString()));
            tmp.append(")");
            u.delete(0,1);
            u.delete(u.length()-1, u.length());
            tmp.append(a(u.toString()).toString());
        }
        return tmp.toString();
    }
    
    StringBuilder a(String u){
        StringBuilder tmp2 = new StringBuilder();
        for(int i=0; i<u.length(); i++){
            if(u.charAt(i)=='('){
                tmp2.append(")");
            }else{
                tmp2.append("(");
            }
        }
        return tmp2;
    }
    
    int split(String p){
        int sum=0;
        for(int i=0; i<p.length(); i++){
            if(p.charAt(i)=='('){
                sum++;
            }if(p.charAt(i)==')'){
                sum--;
            }
            if(sum==0){
                return i+1;
            }
        }
        return p.length();
    }
    
    boolean check (String u){
        int sum=0;
        for(int i=0; i<u.length(); i++){
            if(u.charAt(i)=='('){
                sum++;
            }if(u.charAt(i)==')'){
                sum--;
            }if(sum<0){
                return false;
            }
        }
        if(sum==0){
            return true;
        }else{
            return false;
        }
    }
    
    
}
