package leetcode.dp;

import com.sun.xml.internal.ws.encoding.MtomCodec;

public class P1563_StoneGameV {

    public int StoneGameVDP(int[] stoneValue) {
        //dp[l][r]表示stone[l]~stone[r]进行游戏时获得的最大石子数
        int n = stoneValue.length;
        int[][] dp = new int[n][n];
        int[] sum = new int[n+1];
        for (int i=0; i<n; i++) {
            sum[i+1] = sum[i]+stoneValue[i];
            if (i<n-1){
                dp[i][i+1] = Math.min(stoneValue[i], stoneValue[i+1]);
            }
        }
        for (int len=3; len<=n; len++) {
            for (int l=0; l<=n-len; l++) {
                int r = l+len-1;
                for (int k=l; k<r; k++) {
                    int left = sum[k+1]-sum[l];
                    int right = sum[r+1]-sum[k+1];
                    if (left<right) {
                        dp[l][r] = Math.max(dp[l][r], dp[l][k]+left);
                    } else if (left>right) {
                        dp[l][r] = Math.max(dp[l][r], dp[k+1][r]+right);
                    } else {
                        dp[l][r] = Math.max(dp[l][r], Math.max(dp[l][k], dp[k+1][r])+left);
                    }
                }
            }
        }
        return dp[0][n-1];
    }

    public int stoneGameV(int[] stoneValue) {
        return StoneGameVDP(stoneValue);
    }

    public static void main(String[] args) {
        P1563_StoneGameV solution = new P1563_StoneGameV();
        int[] stoneValue = {6,2,3,4,5,5};
//        int[] stoneValue = {13,1,1,10,5};
        System.out.println(solution.stoneGameV(stoneValue));
    }
}
