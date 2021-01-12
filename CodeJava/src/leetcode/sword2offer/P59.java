package leetcode.sword2offer;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;

class MaxQueue {
    private Deque<Integer> deque;
    private Queue<Integer> queue;

    public MaxQueue() {
        deque = new ArrayDeque<>();
        queue = new ArrayDeque<>();
    }

    public int max_value() {
        if(deque.isEmpty()) {
            return -1;
        }
        return deque.peekFirst();
    }

    public void push_back(int value) {
        while(!deque.isEmpty() && deque.peekLast()<value) {
            deque.pollLast();
        }
        deque.addLast(value);
        queue.add(value);
    }

    public int pop_front() {
        if(deque.isEmpty()) {
            return -1;
        }
        int ans = queue.poll();
        if(ans==deque.peekFirst()) {
            deque.pollFirst();
        }
        return ans;
    }
}

public class P59 {
    public static void main(String[] args) {
        MaxQueue solution = new MaxQueue();
        solution.push_back(1);
        solution.push_back(2);
        System.out.println(solution.max_value());
        System.out.println(solution.pop_front());
        System.out.println(solution.max_value());
    }
}
