# 优先队列
class MinIndexPQ(object):
    def __init__(self, max_n):
        self.n = 0
        self.pq = [0] * (max_n + 1)  #
        self.qp = [-1]*(max_n+1)
        self.keys = [None]*(max_n+1) #保存每个

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def cmp(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def swap(self, i, j):
        a, b = self.pq[i], self.pq[j]
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[a], self.qp[b] = self.qp[b], self.qp[a]

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

    def insert(self, idx, key):
        idx += 1
        self.n += 1
        self.pq[self.n] = idx
        self.qp[idx] = self.n
        self.keys[idx] = key
        self.swim(self.n)

    def delMin(self):
        idx = self.pq[1]
        self.swap(1, self.n)
        self.n -= 1
        self.sink(1)
        # not necessary
        # self.keys[self.pq[self.n+1]] = None
        self.qp[self.pq[self.n+1]] = -1
        return idx

    def delete(self, idx):
        # 删除keys中第idx个元素
        index = self.pq[idx]
        self.swap(index, self.n)
        self.n -= 1
        self.swim(index)
        self.sink(index)
        self.keys[idx] = None
        self.qp[idx] = -1

    def change(self, idx, key):
        idx += 1
        self.keys[idx] = key
        self.swim(self.qp[idx])
        self.sink(self.qp[idx])

    def contains(self, idx):
        idx += 1
        return self.qp[idx] != -1

    def min(self):
        return self.keys[self.pq[1]]

    def min_index(self):
        return self.pq[1]


if __name__ == '__main__':
    import random
    max_pq = MinIndexPQ(10)
    # index = [5, 8, 1, 0, 6, 3, 4]
    index = random.sample(range(0, 10), 7)
    print(index)
    for i, v in enumerate(index):
        max_pq.insert(i, v)
    while not max_pq.is_empty():
        print(max_pq.keys[max_pq.delMin()])
