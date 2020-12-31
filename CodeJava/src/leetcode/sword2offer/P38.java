package leetcode.sword2offer;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

public class P38 {
    List<String> res = new LinkedList<>();
    char[] cArray;

    public void swap(int i, int j) {
        char tmp = cArray[i];
        cArray[i] = cArray[j];
        cArray[j] = tmp;
    }

    public void dfs(int idx) {
        if (idx==cArray.length-1) {
            res.add(String.valueOf(cArray));
            return;
        }
        HashSet<Character> set = new HashSet<>();
        for (int i=idx; i<cArray.length; i++) {
            if (set.contains(cArray[i])) {
                continue;
            }
            set.add(cArray[i]);
            swap(i, idx);
            dfs(idx+1);
            swap(i, idx);
        }
    }

    public String[] permutation(String s) {
        cArray = s.toCharArray();
        dfs(0);
        return res.toArray(new String[res.size()]);
    }
}
