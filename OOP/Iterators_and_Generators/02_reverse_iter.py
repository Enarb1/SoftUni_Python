class reverse_iter:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.start = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1
        if self.start >= 0:
            return self.iterable[self.start]
        raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)