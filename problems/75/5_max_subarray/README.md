https://leetcode.com/problems/maximum-subarray/  

O(n): Keep track of the sum and lowest sum until now, get the best total - min_total  
Better O(n): Negative totals until now wouldn't help the subarray, when total is negative, ditch the previous numbers and set the the subarray start to the current position 