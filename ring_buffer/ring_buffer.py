class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0

    def append(self, item):

        # checking if there is room in ringbuffer, if there is room then append item
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        # else --> there is no room for new item then replace the old itm with old index
        else:
            self.storage[self.oldest_index] = item
            
            # now updating the oldest_index. now oldest_index is the index next to the original index
            if self.oldest_index < self.capacity - 1:
                self.oldest_index += 1
            else:
                self.oldest_index = 0

    def get(self):
        return self.storage
    
    
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']