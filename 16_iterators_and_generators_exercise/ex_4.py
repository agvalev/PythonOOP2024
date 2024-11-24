class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            idx = self.i % len(self.sequence)  # ! this is a formula that keeps us in the range of the text
            self.i += 1
            return self.sequence[idx]
        raise StopIteration
