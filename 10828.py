class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            pop_object = -1
        else:
            pop_object = self.stack.pop()

        return pop_object

    def top(self):
        top_object = None
        if self.isEmpty():
            top_object = -1
        else:
            top_object = self.stack[-1]

        return top_object

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

    def size(self):
        return len(self.stack)


import sys

N = int(sys.stdin.readline())
stack = Stack()

for i in range(N):
    data = sys.stdin.readline().strip()
    if data.startswith("push"):
        _, num = data.split()
        stack.push(int(num))

    elif data.startswith("pop"):
        print(stack.pop())

    elif data.startswith("top"):
        print(stack.top())

    elif data.startswith("empty"):
        if stack.isEmpty():
            print(1)
        else:
            print(0)

    elif data.startswith("size"):
        print(stack.size())

