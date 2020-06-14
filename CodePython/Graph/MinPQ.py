# 优先队列
class MinPQ(object):
    def __init__(self, maxN):
        self.n = 0
        self.pq = [None] * (maxN + 1)

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def cmp(self, i, j):
        return self.pq[i] > self.pq[j]

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def swim(self, idx):
        while idx > 1 and self.cmp(idx // 2, idx):
            self.swap(idx // 2, idx)
            idx = idx // 2

    def sink(self, idx):
        while 2 * idx <= self.n:
            child = 2 * idx
            if child < self.n and self.cmp(child, child + 1):
                child += 1
            if self.cmp(idx, child):
                self.swap(idx, child)
                idx = child
            else:
                break

    def insert(self, key):
        self.n += 1
        self.pq[self.n] = key
        self.swim(self.n)

    def delMin(self):
        max_key = self.pq[1]
        self.swap(1, self.n)
        self.n -= 1
        self.sink(1)
        # not necessary
        # self.pq[self.n+1] = None
        return max_key


if __name__ == '__main__':
    import random
    max_pq = MinPQ(10)
    index = random.sample(range(0, 10), 7)
    for v in index:
        max_pq.insert(v)
    while not max_pq.is_empty():
        print(max_pq.delMin())
