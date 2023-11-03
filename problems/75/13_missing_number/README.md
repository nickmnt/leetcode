https://leetcode.com/problems/missing-number/  
  
O(n): XOR anything xor itself is 0 therefore we can xor the list [0, n] with this list   
O(n): Sum anything negative itself is 0 therefore we can substract our list from [0, n]. We can do this over the for loop step by step!