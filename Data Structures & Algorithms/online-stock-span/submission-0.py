class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        self.stocks.append(price)

        span_stocks = []
        res = 0

        while self.stocks and self.stocks[-1] <= price:
            span_stocks.append(self.stocks.pop())
            res += 1

        while span_stocks:
            self.stocks.append(span_stocks.pop())

        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)