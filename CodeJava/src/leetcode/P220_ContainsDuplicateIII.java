package leetcode;

import java.util.Set;
import java.util.TreeSet;

public class P220_ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> set = new TreeSet<>();
        for (int i=0; i<nums.length; i++) {
            // 找到nums[i]的后继元素
            Long cur = (long)nums[i];
            Long s = set.ceiling(cur);
            if (s!=null && s<=cur+t) {
                return true;
            }
            // 找到nums[i]的前趋元素
            Long g = set.floor(cur);
            if (g!=null && cur<=g+t) {
                return true;
            }
            set.add(cur);
            if (set.size() > k) {
                Long removeNum = (long)nums[i-k];
                set.remove(removeNum);
            }
        }
        return false;
    }

    public static void main(String[] args) {

    }


}
