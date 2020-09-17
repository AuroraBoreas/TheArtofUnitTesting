class Calculator:
    _sum: int = 0
    def add(self, number: int) -> None:
        self._sum += number
    def sum(self) -> int:
        temp = self._sum
        self._sum = 0
        return temp