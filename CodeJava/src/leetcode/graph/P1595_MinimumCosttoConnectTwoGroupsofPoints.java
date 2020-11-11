package leetcode.graph;

import java.util.*;

public class P1595_MinimumCosttoConnectTwoGroupsofPoints {
    public int connectTwoGroups(List<List<Integer>> cost) {
        Map<String, Integer> map = new HashMap<>();
        int rows = cost.size();
        int cols = cost.get(0).size();
        Set<Integer> colSelect = new HashSet<>();
        // 先找左侧组每个数字和右侧 组数字相连的最小值
        for (int r=0; r<rows; r++) {
            int cur = Integer.MAX_VALUE;
            int col = 0;
            for (int c=0; c<cols; c++) {
                if (cur>cost.get(r).get(c)) {
                    cur = cost.get(r).get(c);
                    col = c;
                }
            }
            colSelect.add(col);
            map.put(Integer.toString(r)+"-"+Integer.toString(col), cur);
        }
        for (int c=0; c<cols; c++) {
            // 在左侧组已经连接的节点不再考虑
            if (colSelect.contains(c)){
                continue;
            }
            int cur = Integer.MAX_VALUE;
            int row = 0;
            for (int r=0; r<rows; r++) {
                if (cur>cost.get(r).get(c)) {
                    cur = cost.get(r).get(c);
                    row = r;
                }
            }
            map.put(Integer.toString(row)+"-"+Integer.toString(c), cur);
        }
        int ans = 0;
        for (String key : map.keySet()) {
            ans += map.get(key);
        }
        return ans;
    }

    public static void main(String[] args) {
        List<List<Integer>> costs = new ArrayList<>();
        List<Integer> listA = Arrays.asList(2,5,1);
        List<Integer> listB = Arrays.asList(3,4,7);
        List<Integer> listC = Arrays.asList(8,1,2);
        List<Integer> listD = Arrays.asList(6,2,4);
        List<Integer> listE = Arrays.asList(3,8,8);
        costs.add(listA);
        costs.add(listB);
        costs.add(listC);
        costs.add(listD);
        costs.add(listE);
        P1595_MinimumCosttoConnectTwoGroupsofPoints solution = new P1595_MinimumCosttoConnectTwoGroupsofPoints();
        System.out.println(solution.connectTwoGroups(costs));
    }
}
