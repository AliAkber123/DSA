"""
Day 1 • Arrays • Prefix sums
LeetCode 1480 — Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Given a list nums, return a list where each element is the sum of all
elements from index 0 through the current index.

Example: [1, 2, 3, 4] -> [1, 3, 6, 10]

After solving, fill in:
Approach: TODO
Time complexity: O(?)
Space complexity: O(?)

Run from project root:
    python 01_arrays/001_running_sum.py
These tests are expected to fail until you write your solution.
"""

import unittest


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # TODO: Implement this yourself. Do not change the method name.
        raise NotImplementedError("Write the prefix-sum solution")


class TestRunningSum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(Solution().runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_single_item(self):
        self.assertEqual(Solution().runningSum([5]), [5])

    def test_negatives_and_zero(self):
        self.assertEqual(Solution().runningSum([-2, 0, 3]), [-2, -2, 1])


if __name__ == "__main__":
    unittest.main()
