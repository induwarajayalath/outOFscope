data = 0
key = 0


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(self, data):
    count = 1
    if self.val:
        if data <= self.val:
            if self.left is None:
                self.left = Node(data)
                count = count + 1
                return count
            else:
                p = insert(self.left, data)
                return count + p
        elif data > self.val:
            if self.right is None:
                self.right = Node(data)
                count = count + 1
                return count
            else:
                q = insert(self.right, data)
                return count + q
    else:
        self.val = data
        return 0


len = int(input())

if len == 0:
    print(0)
else:
    arr1 = []  # to store input
    arr1 = input().split()
    # print(arr1)

    arr2 = []  # to store output

    r = Node(int(arr1[0]))
    arr2.append(1)

    for i in range(1, len):
        k = insert(r, int(arr1[i]))
        arr2.append(k)

    for i in range(0, len):
        print(arr2[i], " ", end='')
