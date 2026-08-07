class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.buffer = [None] * k
        self.write_idx = 0
        self.read_idx = 0
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.buffer[self.write_idx] = value
        self.write_idx = (self.write_idx + 1) % self.capacity
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.buffer[self.read_idx] = None
        self.size -= 1
        self.read_idx = (self.read_idx + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.read_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.write_idx - 1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()