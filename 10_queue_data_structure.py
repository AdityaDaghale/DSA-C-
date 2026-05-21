"""Queue Data Structure - FIFO"""

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove from front"""
        return self.items.pop(0) if not self.is_empty() else None
    
    def front(self):
        """View front item"""
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print("Queue:", self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    print("Dequeued:", q.dequeue())
    print("Front:", q.front())
    q.display()
