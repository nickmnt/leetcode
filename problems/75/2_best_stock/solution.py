class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x_min = 10000000
        top_profit = -9999999

        for index, price in enumerate(prices):
            if price < x_min:
                x_min = price

            if x_min != 10000000:
                profit = price - x_min 

                if profit > top_profit:
                    top_profit = profit

        return max(top_profit, 0)
        