class Que():
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            pop_object = -1
        else:
            self.stack.reverse()
            pop_object = self.stack.pop()
            self.stack.reverse()

        return pop_object

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

    def size(self):
        return len(self.stack)

    def back(self):
        back_object = None
        if self.isEmpty():
            back_object = -1
        else:
            back_object = self.stack[-1]
        return back_object

    def front(self):
        front_object = None
        if self.isEmpty():
            front_object = -1
        else:
            front_object = self.stack[0]
        return front_object

import sys

N = int(sys.stdin.readline())
que = Que()

for i in range(N):
    data = sys.stdin.readline().strip()
    if data.startswith("push"):
        _, num = data.split()
        que.push(int(num))

    elif data.startswith("pop"):
        print(que.pop())

    elif data.startswith("size"):
        print(que.size())

    elif data.startswith("empty"):
        if que.isEmpty():
            print(1)
        else:
            print(0)

    elif data.startswith("front"):
        print(que.front())

    elif data.startswith("back"):
        print(que.back())