package leetcode;

import java.util.*;
import java.util.stream.Collectors;

// 题目：给定n个数值在1到n的数字, 计算最小次数使得给定的n个数字按升序排列.
public class MinExchange {

    public void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public boolean correctPos(int[] nums, int idx, Map<Integer, Integer> startIdx){
        int curVal = nums[idx];
        if(curVal==0){
            return idx<startIdx.get(curVal+1);
        }else if(curVal==nums.length-1){
            return idx>=startIdx.get(curVal);
        }else{
            return startIdx.get(curVal)<= idx && idx<startIdx.get(curVal+1);
        }
    }

    public int MinExchangeCnt(int[] nums){
        // step1. 统计1~n中每个数字在nums的出现次数
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int curVal = nums[i];
            map.put(curVal, map.getOrDefault(curVal,0)+1);
        }
        // step2. 计算1~n中每个数字在排序后数组中的起始位置
        Map<Integer, Integer> startIdx = new HashMap<>();
        startIdx.put(1, 0);
        for(int i=1; i<nums.length; i++){
            startIdx.put(i+1, startIdx.get(i)+map.getOrDefault(i, 0));
        }
        // step3. 遍历nums, 如果nums[i]所处位置不在排序后数组的正确位置, 就应该交换
        int cnt = 0;
        int i = 0;
        while(i<nums.length){
            // 如果nums[i]所在的位置i是nums[i]在排序数组中的位置则不作处理
            if(correctPos(nums, i, startIdx)) {
                i += 1;
                continue;
            }
            // 遍历nums[i]应该所处位置区间的每个位置j
            for(int j= startIdx.get(nums[i]); j<nums.length; j++){
                // 如果nums[j]也不在正确位置, 则和nums[i]交换位置
                if(!correctPos(nums, j, startIdx)){
                    cnt += 1;
                    swap(nums, i, j);
                    // 只交换1次
                    break;
                }
            }
            // 如果交换后新的nums[i]已经在正确位置
            if(correctPos(nums, i, startIdx)){
                i += 1;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        MinExchange solution = new MinExchange();
//        int[] nums = {2, 1, 4, 2, 1};
//        int[] nums = {2, 1, 4, 4, 1};
        int[] nums = {4, 3, 2, 1, 1};
        int ans = solution.MinExchangeCnt(nums);
        System.out.println(ans);
    }
}
