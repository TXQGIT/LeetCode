package leetcode.unionfind;

public class P765_CouplesHoldingHands {

    public int minSwapsCouples(int[] row) {
        int n = row.length/2;
        UnionFind unionFind = new UnionFind(n);
        for(int i=0; i<row.length; i+=2){
            unionFind.union(row[i]/2, row[i+1]/2);
        }
        int circle = 0;
        for(int i=0; i<n; i++){
            if(unionFind.parent[i]==i){
                circle++;
            }
        }
        return n-circle;
    }

    public static void main(String[] args) {
        P765_CouplesHoldingHands solution = new P765_CouplesHoldingHands();
        int[] row = {0, 2, 1, 3};
        System.out.println(solution.minSwapsCouples(row));
    }

}
