"""Stack Data Structure - LIFO"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        """View top item"""
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print("Stack:", self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped:", stack.pop())
    print("Peek:", stack.peek())
    stack.display()
