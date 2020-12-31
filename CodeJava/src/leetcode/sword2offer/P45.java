package leetcode.sword2offer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P45 {
    public String minNumber(int[] nums) {
        List<String> strList = new ArrayList<>(nums.length);
        for (int i=0; i<nums.length; i++) {
            strList.add(String.valueOf(nums[i]));
        }
        strList.sort((x,y)->(x+y).compareTo(y+x));
        String ans = String.join("", strList);;
        return ans;
    }

    public static void main(String[] args) {
        int[] nums = {3,30,34,5,9};
        P45 solution = new P45();
        System.out.println(solution.minNumber(nums));
    }
}
