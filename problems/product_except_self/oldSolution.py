class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        result = [0] * n
        prefix = [nums[0]] * n
        postfix = [nums[n-1]] * n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
        for i in reversed(range(0,n-1)):
            postfix[i] = postfix[i+1] * nums[i]
        
        for i in range(0,n):
            result[i] = 1
            if i+1 < n:
                result[i] *= postfix[i+1]
            if i-1 >= 0:
                result[i] *= prefix[i-1]
            result[i] = int(result[i])
        return result