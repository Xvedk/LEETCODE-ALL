class MyQueue:

    def __init__(self):
        self.queue = []
        self.length = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1
        

    def pop(self) -> int:
        if not self.empty():
            self.length -= 1
            return self.queue.pop(0)
        return None        
        

    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]
        return None
        

    def empty(self) -> bool:
        if self.length == 0:
            return True
        return False
        
