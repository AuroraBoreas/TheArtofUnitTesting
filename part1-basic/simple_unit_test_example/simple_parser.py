class SimpleParser:
    def __init__(self, numbers: str):
        self.numbers = numbers
    def parse_and_sum(self):
        if not len(self.numbers):
            return 0
        if not ',' in self.numbers:
            return int(self.numbers)
        else:
            raise ValueError('I can only handle 0 or 1 numbers for now!') 