class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = 1
        while abs(n) > 0:
            if n % 2 == 0:
                n /= 2
                x = x * x
            else:
                if n < 0:
                    n += 1
                    result = result / x
                else: 
                    n -= 1
                    result = result * x
                
                n /= 2
                x = x * x

        return result