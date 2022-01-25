class StockPrice:

    def __init__(self):
        self.stock_map = {}

    def update(self, timestamp: int, price: int) -> None:
        self.stock_map[timestamp] = price
        self._current = max(self.stock_map.keys())
        self.max = max(self.stock_map.values())
        self.min = min(self.stock_map.values())

    def current(self) -> int:
        return self.stock_map[self._current]

    def maximum(self) -> int:
        return self.max

    def minimum(self) -> int:
        return self.min

if __name__ == "__main__":
    stock = StockPrice()
    stock.update(1, 10)
    stock.update(2, 5)
    print(stock.min)
    print(stock.max)
    print(stock._current)
    stock.update(1, 3)
    print(stock.min)
    print(stock.max)
    print(stock._current)