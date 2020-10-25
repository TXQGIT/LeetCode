package leetcode.graph;

public class CourseScheduleII210 {

    public int[] findOrder(int numCourses, int[][] prerequisites){
        int[] order = new int[numCourses];
        DiGraph G = new DiGraph(numCourses, prerequisites);
        Topological topological = new Topological(G);
        if(!topological.isDAG()){
            return new int[0];
        }
        int idx = numCourses-1;
        for(int v : topological.order()){
            order[idx--] = v;
        }
        return order;
    }

    public static void main(String[] args) {
        int numCourses = 4;
        int[][] prerequisites = {{1,0},{2,0},{3,1},{3,2}};
        CourseScheduleII210 solution = new CourseScheduleII210();
        System.out.println(solution.findOrder(numCourses, prerequisites));
    }
}
