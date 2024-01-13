class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = [0]
        for i in range(1, len(temperatures)):
            while len(s) > 0 and temperatures[i] > temperatures[s[-1]]:
                lower_temp_i = s.pop()
                res[lower_temp_i] = i - lower_temp_i
            s.append(i)
        return res                
