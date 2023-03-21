package com.BT;

import java.util.LinkedList;
import java.util.Queue;

public class BT_Array {
    private Integer[] nums;

    public BT_Array(Integer[] nums) {
        this.nums = nums;
    }

    /** BFS **/
    public void traverse_levelorder_bfs() {
        if (this.nums.length < 0) return;

        Queue<Integer> q = new LinkedList<>();

        /** initialization **/
        int i_root = 0;
        q.add(i_root);
        while (true) {
            /** end condition **/
            if (q.size() == 0) break; // empty queue

            /** main logic **/
            Integer i = q.poll();
            if (i >= this.nums.length) continue; // out of bound index
            if (this.nums[i] == null) continue;

            System.out.print(this.nums[i] + " ");

            /** data flow **/
            // get left, right nodes
            int i_plus_one = i + 1;
            int i_left_plus_one = i_plus_one * 2;
            int i_right_plus_one = i_plus_one * 2 + 1;

            int i_left = i_left_plus_one - 1;
            int i_right = i_right_plus_one - 1;

            q.add(i_left);
            q.add(i_right);

        }
    }

}