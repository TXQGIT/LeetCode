package leetcode.graph;

import java.util.LinkedList;
import java.util.Queue;

public class P1162_AsFarfromLandasPossible {

    public int posToInt(int r, int c, int n){
        return r*n+c;
    }

    public void walkNeighbor(int r, int c, int n, int[][] grid, boolean[][] visited,  Queue<Integer> queue){
        if(r>=0 && r<n && c>=0 && c<n && grid[r][c]==0 && !visited[r][c]){
            queue.offer(posToInt(r,c,n));
            visited[r][c] = true;
        }
    }

    public int maxDistance(int[][] grid) {
        // 先把所有的陆地都入队，然后从各个陆地同时开始一层一层的向海洋扩散，
        // 那么最后扩散到的海洋就是最远的海洋
        int n = grid.length;
        Queue<Integer> queue = new LinkedList<Integer>();
        boolean[][] visited = new boolean[n][n];
        for(int r=0; r<n; r++){
            for(int c=0; c<n; c++){
                if(grid[r][c]==1){
                    queue.offer(posToInt(r,c,n));
                    visited[r][c] = true;
                }
            }
        }
        if(queue.size()==n || queue.size()==0){
            return -1;
        }
        int step = 0;
        while(!queue.isEmpty()){
            step += 1;
            int curLen = queue.size();
            for(int i=0; i<curLen; i++){
                int node = queue.poll();
                int r = node/n;
                int c = node%n;
                walkNeighbor(r-1, c, n, grid, visited, queue);
                walkNeighbor(r, c-1, n, grid, visited, queue);
                walkNeighbor(r+1, c, n, grid, visited, queue);
                walkNeighbor(r, c+1, n, grid, visited, queue);
            }
        }
        return step-1;
    }

    public static void main(String[] args) {
        P1162_AsFarfromLandasPossible solution = new P1162_AsFarfromLandasPossible();
        int[][] grid = {{1,0,0},{0,0,0},{0,0,0}};
        System.out.println(solution.maxDistance(grid));
    }
}
