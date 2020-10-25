package leetcode.graph;

/* 计算有向存是否存在环 */
public class DirectedCircle {
    // 标记节点是否已被访问过
    private boolean[] visited;
    // 标记当前访问路径包含哪些结点
    private boolean[] onStack;
    // 有向图是否存在环的标记
    private boolean circle;

    public DirectedCircle(DiGraph G) {
        onStack = new boolean[G.V()];
        visited = new boolean[G.V()];
        circle = false;
        for(int v=0; v<G.V(); v++){
            if(!visited[v]){
                dfs(G, v);
            }
        }
    }

    // DFS求有向图是否存在环
    public void dfs(DiGraph G, int v){
        visited[v] = true;
        // 标记v存在于当前dfs路径下
        onStack[v] = true;
        for(int u : G.adj(v)){
            if(this.circle){
                return;
            }else if(!visited[u]){
                dfs(G, u);
            }else if(onStack[u]){
                circle = true;
            }
        }
        // v节点的遍历结束, 将v从当前dfs路径移除
        onStack[v] = false;
    }

    public boolean hasCircle(){
        return this.circle;
    }
}
