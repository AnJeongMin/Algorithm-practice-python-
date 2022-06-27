class Deque:

    front = 0
    rear = 0
    MAX_SIZE = 1000
    q = []

    def __init__(self):
        self.front = 0
        self.rear = 0
        self.q = [0 for _ in range(self.MAX_SIZE)]

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    def is_full(self):
        if (self.rear+1) % self.MAX_SIZE == self.front:
            return True
        return False

    def append(self, x):
        if Deque.is_full(self):
            print("Deque is full")
            return
        self.rear = (self.rear+1) % (self.MAX_SIZE)
        self.q[self.rear] = x
    
    def appendleft(self, x):
        if Deque.is_full(self):
            print("Deque is full")
            return
        self.q[self.front] = x
        self.front = (self.front-1+self.MAX_SIZE) % self.MAX_SIZE
        
    def popleft(self):
        if Deque.is_empty(self):
            print("Deque is empty")
            return
        self.front = (self.front+1) % self.MAX_SIZE
        return self.q[self.front]
    
    def pop(self):
        if Deque.is_empty(self):
            print("Deque is empty")
            return
        result = self.q[self.rear]
        self.rear = (self.rear-1+self.MAX_SIZE) % self.MAX_SIZE
        return result

    def print_dq(self):
        if Deque.is_empty(self):
            print("Deque is empty")
            return
        idx = (self.front+1) % self.MAX_SIZE
        while True:
            if idx == self.rear:
                print(self.q[idx])
                break
            print(self.q[idx], end=' ')
            idx = (idx+1) % self.MAX_SIZE

if __name__ == "__main__":

    dq = Deque()
    dq.append(1)
    dq.append(3)
    dq.appendleft(5)
    dq.pop()
    dq.append(6)
    dq.append(4)
    dq.print_dq()

    