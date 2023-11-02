https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/  
  
O(logn): If sorted (nums[l] < nums[r]) nums[l] is the best local solution. If not sorted, either it is part of left side (nums[m] >= nums[l]) or right side. If on left side, it is defintely to the right of it. If on the right side, it is definetly to the left of it. 