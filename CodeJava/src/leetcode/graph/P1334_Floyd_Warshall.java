package leetcode.graph;

public class P1334_Floyd_Warshall {

    /* 根据边集合创建图的领接矩阵表示 */
    public int[][] buildGraph(int n, int[][] edges){
        int[][] graph = new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                graph[i][j] = Integer.MAX_VALUE;
            }
            graph[i][i] = 0;
        }
        for(int i=0; i<edges.length; i++){
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            graph[u][v] = w;
            graph[v][u] = w;
        }
        return graph;
    }

    /* 计算图中所有节点对之间的最短距离 */
    public int[][] Floyd_Warshall(int n, int[][] graph){
        // 令d_ij(k)表示从i到j的所有中间结点取自{1,2,...,k}的一条最短路径权重
        // d_ij(k) = min(d_ij(k-1), d_ik(k-1)+d_kj(k-1)), when k>=1
        // d_ij(0) = w_ij
        int[][] dist = new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                dist[i][j] = graph[i][j];
            }
        }
        for(int k=0; k<n; k++){
            int[][] newDist = new int[n][n];
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE) {
                        newDist[i][j] = Math.min(dist[i][j], dist[i][k]+dist[k][j]);
                    }else{
                        newDist[i][j] = dist[i][j];
                    }
                }
            }
            dist = newDist;
        }
        return dist;
    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] graph = buildGraph(n, edges);
        int[][] dist = Floyd_Warshall(n, graph);
        int cnt = Integer.MAX_VALUE;
        int ans = 0;
        for(int i=0; i<n; i++){
            int curCnt = 0;
            for(int j=0; j<n; j++){
                if(dist[i][j]<=distanceThreshold){
                    curCnt += 1;
                }
            }
            if(curCnt>0 && curCnt<=cnt){
                cnt = curCnt;
                ans = i;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
//        int n = 4;
//        int[][] edges = {{0,1,3},{1,2,1},{1,3,4},{2,3,1}};
//        int distanceThreshold = 4;
        int n = 5;
        int[][] edges = {{0,1,2},{0,4,8},{1,2,3},{1,4,2},{2,3,1},{3,4,1}};
        int distanceThreshold = 2;
        P1334_Floyd_Warshall solution = new P1334_Floyd_Warshall();
        System.out.println(solution.findTheCity(n, edges, distanceThreshold));
    }
}
