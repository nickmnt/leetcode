https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/  
  
O(n): Use two pointers, if nums[l] + nums[r] > target: must pull right to the left since we want the value to get smaller. If nums[l] + nums[r] < target we pull left to right since we want the value to get bigger.