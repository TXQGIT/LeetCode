package leetcode.sword2offer;

public class P60 {
    public double[] dicesProbability(int n) {
        double[] dp = {1/6d, 1/6d, 1/6d, 1/6d, 1/6d, 1/6d};
        for(int i=2; i<=n; i++) {
            double[] nextDp = new double[5*i+1];
            for(int j=0; j<dp.length; j++) {
                for(int k=0; k<6; k++) {
                    nextDp[j+k] += dp[j]/6;
                }
            }
            dp = nextDp;
        }
        return dp;
    }

    public static void main(String[] args) {
        P60 solution = new P60();
        double[] ans = solution.dicesProbability(2);
        for (double p:ans) {
            System.out.println(p);
        }
    }
}
