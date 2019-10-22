# FIFO: First in, First out
class Queue:
    def __init__(self):
        self.queue = []

    def pop(self): 
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def push(self,val):
        return self.queue.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.size()]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0