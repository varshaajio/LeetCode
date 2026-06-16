class Solution {
    public String processStr(String s) {
      StringBuilder sb=new StringBuilder();
      for(int i=0;i<s.length();i++){
        if(isl(s.charAt(i)))
         sb.append(s.charAt(i));
        if(s.charAt(i)=='*' && !sb.isEmpty()){
          sb.deleteCharAt(sb.length()-1);
        }
        if(s.charAt(i)=='#')
          sb.append(sb.toString());
        if(s.charAt(i)=='%')
          sb.reverse();
        
      }  
      return sb.toString();
    }
    public boolean isl(char ch){
        if(ch>='a' && ch<='z')
         return true;
         return false;
    }
}
