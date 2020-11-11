package leetcode.graph;

import java.util.PriorityQueue;

class DistNode implements Comparable<DistNode>{
    int r;
    int c;
    int dist;
    public DistNode (int r, int c, int dist) {
        this.r = r;
        this.c = c;
        this.dist = dist;
    }

    public int compareTo (DistNode that) {
        if (this.dist==that.dist){
            if (this.r==that.r){
                return this.c - that.c;
            } else {
                return this.r - that.r > 0 ? 1 : -1;
            }
        } else {
            return this.dist - that.dist > 0 ? 1 : -1;
        }
    }
}

public class P1631_PathWithMinimumEffort {
    public int minimumEffortPath(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;
        int[][] delta = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        int[] dist = new int[rows*cols];
        boolean[] seen = new boolean[rows*cols];
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++)
            dist[i*cols+j] = Integer.MAX_VALUE;
        }

        PriorityQueue<DistNode> queue = new PriorityQueue<>();
        queue.offer(new DistNode(0, 0, 0));
        while (!queue.isEmpty()) {
            DistNode distNode = queue.poll();
            int r = distNode.r;
            int c = distNode.c;
            int distance = distNode.dist;
            if (seen[r*cols+c]) {
                continue;
            }
            seen[r*cols+c] = true;
            dist[r*cols+c] = distance;
            for (int i=0; i<4; i++){
                int nr = r + delta[i][0];
                int nc = c + delta[i][1];
                if (nr>=0 && nr<rows && nc>=0 && nc<cols && !seen[nr*cols+nc]) {
                    int tmp = Math.max(distance, Math.abs(heights[r][c]-heights[nr][nc]));
                    queue.offer(new DistNode(nr, nc, tmp));
                }
            }
        }
        return dist[rows*cols-1];
    }

    public static void main(String[] args) {
//        int[][] heights = {{1,2,2},{3,8,2},{5,3,5}};
//        int[][] heights = {{1,2,3},{3,8,4},{5,3,5}};
        int[][] heights = {{1,10,6,7,9,10,4,9}};
        P1631_PathWithMinimumEffort solution = new P1631_PathWithMinimumEffort();
        System.out.println(solution.minimumEffortPath(heights));
    }
}
