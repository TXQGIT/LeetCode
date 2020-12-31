package leetcode.unionfind;

import java.util.PriorityQueue;
import java.util.Queue;

public class P778_SwimInRisingWater {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        int result = 0;
        // 记录下一步可以遍历的位置，用最小堆保证先遍历高度低的位置
        Queue<int[]> minHeap = new PriorityQueue<>((a,b)->(a[0]-b[0]));
        boolean[][] visited = new boolean[n][n];

        int[][] delta = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        minHeap.offer(new int[]{grid[0][0], 0, 0});
        visited[0][0] = true;

        while (!minHeap.isEmpty()) {
            int[] curPos = minHeap.poll();
            result = Math.max(result, curPos[0]);
            if (curPos[1]==n-1&&curPos[2]==n-1) {
                break;
            }
            for (int i=0; i<delta.length; i++) {
                int r = curPos[1]+delta[i][0];
                int c = curPos[2]+delta[i][1];
                if (r>=0&&r<n&&c>=0&&c<n&&!visited[r][c]) {
                    visited[r][c] = true;
                    minHeap.offer(new int[]{grid[r][c], r, c});
                }
            }
        }
        return result;
    }
}
