package leetcode;

class NumArray {
    // 存储初始化数组的长度. 线段树要求数组长度不变, 否则无法使用.
    private int n;
    // 存储原始数组数据和线段树中间层级数据的树.
    private int[] tree;

    public NumArray(int[] nums) {
        // 线段树
        // 长度为数组长度*2
        n = nums.length;
        tree = new int[2*n];
        // 最后n个存储原始数据
        for(int i=n; i<2*n; i++){
            tree[i] = nums[i-n];
        }
        // 前n个存储中间的区间层级数据, 下标为0的元素不用
        for(int i=n-1; i>0; i--){
            tree[i] = tree[2*i]+tree[2*i+1];
        }
    }

    public void update(int i, int val) {
        int idx = i+n;
        int delta = val-tree[idx];
        while(idx>0){
            tree[idx] += delta;
            idx = idx/2;
        }
        return;
    }

    public int sumRange(int i, int j) {
        int left = i+n;
        int right = j+n;
        int ans = 0;
        while(left<=right){
            //如果left为奇数, 说明只能包含left所在区间的一半
            if(left%2==1){
                ans += tree[left];
                left += 1; //移到下一个区间
            }
            //同理如果right为偶数, 说明只能包含right所在区间的一半
            if(right%2==0){
                ans += tree[right];
                right -= 1;
            }
            left = left/2;
            right = right/2;
        }
        return ans;
    }
}

public class RangeSumQuery_Mutable307 {
    public static void main(String[] args){
        int[] array = {1,3,5};
        NumArray solution = new NumArray(array);
        System.out.println(solution.sumRange(0,2));
        solution.update(1,2);
        System.out.println(solution.sumRange(0,2));
    }
}
