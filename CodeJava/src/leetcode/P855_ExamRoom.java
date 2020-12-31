package leetcode;

import java.util.TreeSet;

class ExamRoom {

    int N;
    TreeSet<Integer> students;

    public ExamRoom(int N) {
        this.N  = N;
        this.students = new TreeSet<>();
    }

    public int seat() {
        int student = 0;
        if (students.size()>0) {
            int dist = students.first();
            Integer pre = null;
            for (Integer s: students) {
                if (pre!=null) {
                    int d = (s-pre)/2;
                    if (d>dist) {
                        dist = d;
                        student = pre+d;
                    }
                }
                pre = s;
            }
            if (N-1-students.last()>dist) {
                student = N-1;
            }
        }
        students.add(student);
        return student;
    }

    public void leave(int p) {
        students.remove(p);
    }
}

public class P855_ExamRoom {
    public static void main(String[] args) {
        ExamRoom solution = new ExamRoom(10);
        System.out.println(solution.seat());
        System.out.println(solution.seat());
        System.out.println(solution.seat());
        System.out.println(solution.seat());
        solution.leave(4);
        System.out.println(solution.seat());
    }
}
