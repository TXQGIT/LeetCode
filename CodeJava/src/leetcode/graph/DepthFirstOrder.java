package leetcode.graph;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/* 计算有向图深度有向遍历下的前序、后序和逆后序结果 */
public class DepthFirstOrder {
    private boolean[] visited;
    private Queue<Integer> pre;
    private Queue<Integer> post;
    private Stack<Integer> reversePost;

    public DepthFirstOrder(DiGraph G){
        pre = new LinkedList<>();
        post = new LinkedList<>();
        reversePost = new Stack<>();
        visited = new boolean[G.V()];
        for(int v=0; v<G.V(); v++){
            if(!visited[v]){
                dfs(G, v);
            }
        }
    }

    public void dfs(DiGraph G, int v){
        pre.offer(v);
        visited[v] = true;
        for(int u : G.adj(v)){
            if(!visited[u]){
                dfs(G, u);
            }
        }
        post.offer(v);
        reversePost.push(v);
    }

    public Iterable<Integer> pre(){
        return this.pre;
    }

    public Iterable<Integer> post(){
        return this.post;
    }

    public Iterable<Integer> reversepost(){
        return this.reversePost;
    }
}
