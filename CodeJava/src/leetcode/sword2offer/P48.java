package leetcode.sword2offer;

import java.util.HashMap;
import java.util.Map;

public class P48 {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int lastRepeatIdx = -1;
        Map<Character, Integer> map = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            Character c = s.charAt(i);
            if (map.containsKey(c)) {
                lastRepeatIdx = Math.max(lastRepeatIdx, map.get(c));
            }
            result = Math.max(result, i-lastRepeatIdx);
            map.put(c, i);
        }
        return result;
    }

    public static void main(String[] args) {
        P48 solution = new P48();
        String s = "abcabcdbea";
//        String s = "abcabcaa";
        System.out.println(solution.lengthOfLongestSubstring(s));
    }
}
