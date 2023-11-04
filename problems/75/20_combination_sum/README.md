https://leetcode.com/problems/combination-sum/  
    
At each depth in the tree, do not reuse previous candidates  
  
space complexity is O(target val / smallest val in candidates) b/c max depth of the tree is when it keeps adding the smallest element to the combination until it hits or exceeds target. 

time: O(number of candidates^max depth)

