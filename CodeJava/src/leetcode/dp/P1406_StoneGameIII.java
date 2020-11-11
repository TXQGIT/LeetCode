package leetcode.dp;

import org.omg.Messaging.SYNC_WITH_TRANSPORT;

public class P1406_StoneGameIII {

    public String stoneGameIII(int[] stoneValue) {
        //dp[i][0]:表示在stone[i:]进行游戏,先手可取前3堆石子时,先手获得最大石子数
        //dp[i][1]:表示在stone[i:]进行游戏,先手可取前3堆石子时,后手获得最大石子数
        int n = stoneValue.length;
        int[][] dp = new int[n+1][2];
        //由于stone的值存在负数, 而且每次必须取数, 所以dp的值存在负数
        for (int i=0; i<=n; i++) {
            dp[i][0] = Integer.MIN_VALUE;
            dp[i][1] = Integer.MIN_VALUE;
        }
        dp[n][0] = dp[n][1] = dp[n-1][1] = 0;
        dp[n-1][0] = stoneValue[n-1];
        for (int i=n-2; i>=0; i--) {
            //记录stone[i]为起点的前x项和
            int curSelectSum = 0;
            //记录前x项中的最优选择, 为了计算dp[i][1]
            int selectX = 1;
            for (int j=1; j<=3; j++) {
                if (i+j<=n){ //保证不越界
                    curSelectSum += stoneValue[i+j-1];
                    if (dp[i][0] < curSelectSum+dp[i+j][1]){
                        dp[i][0] = curSelectSum+dp[i+j][1];
                        selectX = j;
                    }
                }
            }
            dp[i][1] = dp[i+selectX][0];
        }
        if (dp[0][0]>dp[0][1]) {
            return "Alice";
        } else if (dp[0][0]<dp[0][1]){
            return "Bob";
        } else {
            return "Tie";
        }
    }

    public static void main(String[] args) {
//        int[] values = {1,2,3,7};
//        int[] values = {1,2,3,-9};
//        int[] values = {1,2,3,-1,-2,-3,7};
        int[] values = {-3,4,-3,10,4,11,-14,12,-10,-6,7,3,-1,-13,-4,11,-9,-8,11,-11,12,9,3};
        P1406_StoneGameIII solution = new P1406_StoneGameIII();
        System.out.println(solution.stoneGameIII(values));
    }

}
