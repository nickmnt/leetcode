https://leetcode.com/problems/reverse-linked-list/  
  
mySolution: If any one them is None, return the other. The head elem is the smallest of the two heads. Keep going forward until one of the heads is None. Select the head that is smaller than the other and keep going forward as long as the values next of that head are still smaller than the other head, then set the next value to the other head (because it is bigger than the next value) and move on from this by setting the head to tmp (next) because it has been finalized.

solution: Use dummy node at first to just iteratively select the smallest node and point to it using next. At the end, we have to add the remainder of the one that is not None to the tail.