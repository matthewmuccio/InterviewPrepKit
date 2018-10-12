#!/usr/bin/env python3


class MyQueue(object):
    def __init__(self):
        self.head = []
        self.tail = []
    def peek(self):
        self.digest()
        return self.tail[-1]
    def pop(self):
        self.digest()
        return self.tail.pop()
    def put(self, value):
        self.head.append(value)
    def digest(self):
        if not self.tail:
            for _ in range(len(self.head)):
                self.tail.append(self.head.pop())


if __name__ == "__main__":
    queue = MyQueue()
    t = int(input())
    for line in range(t):
        values = map(int, input().split())
        values = list(values)
        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())
