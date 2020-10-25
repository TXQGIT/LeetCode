package leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

public class RemoveInvalidParentheses301 {

    public boolean is_vaild(String s){
        int count = 0;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='('){
                count += 1;
            }
            if(s.charAt(i)==')'){
                count -= 1;
            }
            if(count<0){
                return false;
            }
        }
        return count==0;
    }

    public List<String> removeInvalidParentheses(String s) {
        //BFS
        //第1层:判断原始序列s是不是有效,有效就结束;否则从s中提出一个字符得到序列数组level.
        //第2层:判断level中是否存在有效序列,如果存在就结束并返回有效的序列;
        //  否则将level中每个序列再剔除1个字符. 依次循环直到求得答案.
        HashSet<String> level = new HashSet<String>();
        level.add(s);
        List<String> ans = new ArrayList<String>();
        while(level.size()>0){
            Iterator it = level.iterator();
            while(it.hasNext()){
                String cur = (String)it.next();
                if(is_vaild(cur)){
                    ans.add(cur);
                }
            }
            if(ans.size()>0){ break; }

            HashSet<String> next_level = new HashSet<String>();
            it = level.iterator();
            while(it.hasNext()){
                String cur = (String)it.next();
                for(int i=0; i<cur.length(); i++){
                    if(cur.charAt(i)=='(' || cur.charAt(i)==')'){
                        String tmp_str = cur.substring(0,i)+cur.substring(i+1, cur.length());
                        next_level.add(tmp_str);
                    }
                }
            }
            level = next_level;
        }
        return ans;
    }

    public static void main(String[] args){
        RemoveInvalidParentheses301 solution = new RemoveInvalidParentheses301();
        String s = "()())()";
        System.out.println(solution.removeInvalidParentheses(s));
    }
}
