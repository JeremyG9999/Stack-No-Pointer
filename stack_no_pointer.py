class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)  
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")  
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def print_stack(self):
        for item in self.items:
            print(item)
def main():
    stacks = Stack()
    stacks.push(8)
    stacks.push(7)
    stacks.push(6)
    stacks.push(5)
    stacks.pop()
    print("Stack:")
    stacks.print_stack()
    print("Stack Size:")
    print(stacks.size())
main()