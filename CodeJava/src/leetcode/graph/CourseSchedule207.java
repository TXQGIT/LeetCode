package leetcode.graph;

public class CourseSchedule207 {

    public boolean canFinish(int numCourses, int[][] prerequisites){
        DiGraph G = new DiGraph(numCourses, prerequisites);
        DirectedCircle circleFinder = new DirectedCircle(G);
        return !circleFinder.hasCircle();
    }

    public static void main(String[] args){
        int numCourses = 3;
        int[][] prerequisites = {{1, 0}};
        CourseSchedule207 solution = new CourseSchedule207();
        System.out.println(solution.canFinish(numCourses, prerequisites));
    }
}
