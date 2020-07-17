class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            print(f"data: {self.data}, index: {self.index}")
            self.data[self.index] = item

            if [self.index] == [self.capacity - 1]:
                self.index = 0
            else:
                self.index += 1
        else:
            self.data.append(item)

    def get(self):
        return self.data