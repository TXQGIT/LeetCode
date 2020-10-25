package leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

class FenwickTree{

    private int n;

    private int[] tree;

    public FenwickTree(int size){
        n = size;
        tree = new int[size];
    }

    public int low_bit(int x){
        return x&(-x);
    }

    public void update(int idx, int delta){
        while(idx<n){
            tree[idx] += delta;
            idx += low_bit(idx);
        }
    }

    public int search(int idx){
        int ans = 0;
        while(idx>0){
            ans += tree[idx];
            idx -= low_bit(idx);
        }
        return ans;
    }

}

class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        // 树状数组
        // 令prefix表示nums中前缀和
        // lower <= prefix[right] - prefix[left] <= upper (公式1)
        // prefix[right]-lower >= prefix[left] >= prefix[right]-upper (公式2)

        // 对每个prefix[right],
        // 计算在该prefix之前有多少前缀和x在[prefix[right]-upper, prefix[right]-lower]
        // 对于满足条件的x, 则prefix[right]-x一定满足公式1.

        // 而计算在该prefix之前有多少前缀和x在[prefix[right]-upper, prefix[right]-lower],
        // 等价于315题-计算右侧小于当前元素的个数 计算两次.
        int n = nums.length;
        // 计算前缀和
        long[] prefix = new long[n];
        prefix[0] = nums[0];
        for(int i=1; i<n; i++){
            prefix[i] = prefix[i-1]+nums[i];
        }
        // 离散化
        Set<Long> set = new TreeSet<>();
        for(long val: prefix){
            set.add(val);
            set.add(val-lower);
            set.add(val-upper);
        }
        Map<Long, Integer> map = new HashMap<>();
        int rank = 1;
        for(Long v : set){
            map.put(v, rank++);
        }
        // 树状数组初始化
        FenwickTree tree = new FenwickTree(rank);
        int ans = 0;
        for(long val:prefix){
            int high_rank = map.get(val-lower);
            int low_rank = map.get(val-upper);
            ans += tree.search(high_rank)-tree.search(low_rank-1);
            rank = map.get(val);
            tree.update(rank, 1);
        }
        return ans;
    }
}

public class CountofRangeSum327 {
    public static void main(String[] args){
        Solution solution = new Solution();
        int[] nums = {-2,5,-1};
        int lower = -2;
        int upper = 2;
        solution.countRangeSum(nums, lower, upper);
    }

}