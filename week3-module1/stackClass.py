class my_stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def is_full(self):
        return len(self._stack) == self._capacity

    def push(self, value):
        if self.is_full():
            print('Overflow')
        else:
            self._stack.append(value)

    def pop(self):
        if self.is_empty():
            print('Underflow')
        else:
            self._stack.pop()

    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        return self._stack[-1]

if __name__ == "__main__":
    my_stack1 = my_stack(4)
    print(my_stack1.is_empty())
    my_stack1.push(5)
    print(my_stack1.is_empty())
    my_stack1.pop()
    print(my_stack1.is_empty())
    my_stack1.push(5)
    my_stack1.push(4)
    print(my_stack1.top())
