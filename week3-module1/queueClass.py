class my_queue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def is_full(self):
        return len(self._queue) == self._capacity

    def enqueue(self, value):
        if self.is_full():
            print('Overflow')
        else:
            self._queue.append(value)

    def dequeue(self):
        if self.is_empty():
            print('Underflow')
        else:
            self._queue.pop(0)

    def front(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self._queue[0]


if __name__ == "__main__":
    my_queue1 = my_queue(5)
    print(my_queue1.is_empty())
    print(my_queue1.is_full())

    my_queue1.enqueue(5)
    my_queue1.enqueue(3)
    my_queue1.enqueue(2)
    my_queue1.enqueue(1)
    my_queue1.enqueue(1)
    print(my_queue1.front())
    print(my_queue1.is_full())

    my_queue1.dequeue()
    print(my_queue1.front())
