import os

# task_1

n = 10

class Square:
    def __init__(self, max) -> None:
        self.max = max

    def __iter__(self):
        self.cur = 0
        return self
    
    def __next__(self):
        if self.cur < self.max:
            self.cur += 1
            return self.cur ** 2
        raise StopIteration

def square(max):
    for num in range(1, max + 1):
        yield num ** 2

square_compr = (num ** 2 for num in range(1, n + 1))

# task_2

def gen_files_path(directory, start='/'):
    for t in os.walk(start):
        if directory in t[1]:
            break
        else:
            for file in t[2]:
                print(os.path.join(t[0], file))

# task_3

def count_strs_python(directory='/'):
    for t in os.walk(directory):
        for file in t[2]:
            if file.endswith('.py'):
                with open(os.path.join(t[0], file)) as f:
                    length = len(f.readlines())
                yield length

# task_4

class LinkedList:
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            if self.head is self.tail:
                self.head.next = self.tail
            self.tail.next = Node(value)
            self.tail = self.tail.next


    def get(self, index):
        cur_node = self.head
        cur_index = 0

        while cur_node != None:
            if cur_index == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_index += 1
        
        return -1

    def remove(self, index):
        cur_node = self.head
        prev_node = None
        cur_index = 0
        
        while cur_index != index:
            if not cur_node:
                return False
            prev_node = cur_node
            cur_node = cur_node.next
            cur_index += 1

        if not prev_node:
            self.tail = None
            self.head = None
        elif self.head is cur_node:
            self.head = cur_node.next
        elif self.tail is cur_node:
            self.tail = prev_node
            prev_node.next = None
        else:
            prev_node.next = cur_node.next
        return True

    def __iter__(self):
        return self
    
    def __next__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node.data
            cur_node = cur_node.next

    def __str__(self) -> str:
        cur_node = self.head

        values = []
        while cur_node != None:
            values.append(str(cur_node.data))
            cur_node = cur_node.next

        return " ".join(values)

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

# task_5

with open('bad_logs.logs', 'w+') as bad, open('logs.logs', 'r') as logs:
    for line in logs.readlines():
        if 'ERROR' in line:
            bad.write(line)