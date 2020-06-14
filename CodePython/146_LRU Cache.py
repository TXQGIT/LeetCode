class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key  # 删除hashMap中节点使用
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        node = self.hashMap.get(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.move_node_to_tail(key)
        res = self.hashMap.get(key, None)
        if res:
            return res.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.move_node_to_tail(key)
            self.hashMap.get(key).val = value
        else:
            if len(self.hashMap) >= self.capacity:
                delete_node = self.head.next
                self.head.next = delete_node.next
                delete_node.next.prev = self.head
                self.hashMap.pop(delete_node.key)
            node = ListNode(key, value)
            self.hashMap[key] = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))