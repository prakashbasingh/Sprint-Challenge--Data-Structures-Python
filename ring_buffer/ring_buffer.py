class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_item = 0

    def append(self, item):
        if(len(self.storage) == self.capacity):
            self.storage[self.oldest_item] = item
            if(self.oldest_item < self.capacity - 1):
                self.oldest_item += 1
            else:
                self.oldest_item = 0

    def get(self):
        return self.storage
    
    
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']