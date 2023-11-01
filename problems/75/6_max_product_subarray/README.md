https://leetcode.com/problems/maximum-product-subarray/  
  
O(n): Use two arrays, maximum product and min product, keep calculating the max and min product before i.  
Each time we have (max and min product before i) item[i] (... item[n-1]).  
Now calculate max and min product for item[i] using the max and min values between item[i], max[i-1], min[i-1].  
Use cur_min and cur_max as we just need to have to previous result and don't need to store all,.