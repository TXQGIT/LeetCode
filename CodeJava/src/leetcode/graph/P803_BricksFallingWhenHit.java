package leetcode.graph;

import java.util.*;

public class P803_BricksFallingWhenHit {

    Map<Integer, Set<Integer>> graph;

    Map<Integer, Integer> inDegree;

    public void buildGraph(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        this.graph = new HashMap<>();
        this.inDegree = new HashMap<>();
        graph.put(-1, new HashSet<>());
        int[][] delta = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (int r=0; r<rows; r++) {
            for (int c=0; c<cols; c++) {
                if (grid[r][c]==0) {
                    continue;
                }
                if (!graph.containsKey(r*cols+c)) {
                    graph.put(r*cols+c, new HashSet<>());
                }
                if (r==0) {
                    inDegree.put(c, inDegree.getOrDefault(c,0)+1);
                }
                for (int i=0; i<delta.length; i++) {
                    int nextR = r+delta[i][0];
                    int nextC = c+delta[i][1];
                    if (nextR>=0 && nextR<rows && nextC>=0 && nextC<cols && grid[nextR][nextC]==1) {
                        graph.get(r*cols+c).add(nextR*cols+nextC);
                        inDegree.put(nextR*cols+nextC, inDegree.getOrDefault(nextR*cols+nextC,0)+1);
                    }
                }
            }
        }
    }

    public int BFS(Queue<Integer> zeroInDegreeQueue) {
        int count = 0;
        while (!zeroInDegreeQueue.isEmpty()) {
            count += 1;
            Integer node = zeroInDegreeQueue.poll();
            Iterator it = graph.get(node).iterator();
            while (it.hasNext()) {
                Integer adj = (Integer) it.next();
                it.remove();
                graph.get(adj).remove(node);
                inDegree.put(adj, inDegree.get(adj) - 1);
                if (inDegree.get(adj) == 0) {
                    zeroInDegreeQueue.offer(adj);
                }
            }
        }
        return count;
    }

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int rows = grid.length;
        int cols = grid[0].length;
        buildGraph(grid);
        int[] results = new int[hits.length];
        Queue<Integer> zeroInDegreeQueue = new ArrayDeque<>();
        for (int i=0; i<hits.length; i++) {
            int r = hits[i][0];
            int c = hits[i][1];
            Iterator it = graph.get(r*cols+c).iterator();
            while (it.hasNext()) {
                Integer adj = (Integer) it.next();
                it.remove();
                inDegree.put(adj, inDegree.get(adj) - 1);
                if (inDegree.get(adj) == 0) {
                    zeroInDegreeQueue.offer(adj);
                }
            }
            results[i] = BFS(zeroInDegreeQueue);
        }
        return results;
    }

    public static void main(String[] args) {
        P803_BricksFallingWhenHit solution = new P803_BricksFallingWhenHit();
        int[][] grid = {{1,0,0,0}, {1,1,1,0}};
        int[][] hits = {{1,0}};
        int[] results = solution.hitBricks(grid, hits);
        System.out.println(results);
    }
}
